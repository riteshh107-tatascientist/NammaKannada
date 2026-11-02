import io
import json
import random
import re
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import streamlit as st

from data import ALL_ITEMS, LESSONS, PHRASES

st.set_page_config(page_title="NammaKannada", page_icon="📘", layout="wide")

DATA_DIR = Path(__file__).parent / "user_data"
DATA_DIR.mkdir(exist_ok=True)
PAGES = ["Home", "Learn Kannada", "Phrasebook", "Flashcards", "Practice Quiz", "My Progress", "About Project"]

# ---------------------------------------------------------------- styling
st.markdown(
    """
<style>
.stApp {background:#f5f8fd;}
h1,h2,h3 {color:#0f3d75 !important;}
[data-testid="stSidebar"] {background:#ffffff;}
.stRadio label p, .stRadio label span, .stRadio label div {color:#0f172a !important; font-size:1.05rem;}
.stButton>button {background:#1565c0; color:#fff; border:0; border-radius:10px; padding:.5rem 1.2rem; font-weight:600;}
.stButton>button:hover {background:#0d47a1; color:#fff;}
.hero {background:linear-gradient(135deg,#0f3d75,#1e88e5); color:#fff; padding:28px 32px; border-radius:18px; margin-bottom:18px;}
.hero h1 {color:#fff !important; margin:0;}
.hero p {color:#e3f2fd; margin:6px 0 0 0; font-size:1.05rem;}
.card {background:#fff; border:1px solid #e3eaf5; border-radius:14px; padding:16px 20px; margin-bottom:12px;}
.kn {font-size:2rem; color:#0f3d75; font-weight:700; line-height:1.3;}
.tr {color:#1565c0; font-style:italic;}
.big-kn {font-size:3.2rem; color:#0f3d75; font-weight:700; text-align:center;}
.flash {background:#fff; border:2px solid #bbdefb; border-radius:18px; padding:36px 20px; text-align:center; margin:10px 0;}
.badge {display:inline-block; background:#e3f2fd; color:#0f3d75; border-radius:20px; padding:6px 14px; margin:4px; font-weight:600;}
.badge.off {background:#eceff1; color:#90a4ae;}
.foot {text-align:center; color:#607d8b; font-size:.85rem; margin-top:40px;}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- progress storage
def default_progress():
    return {"xp": 0, "streak": 0, "last_day": None, "lessons_done": [], "history": [], "cards": {}, "words_seen": 0}


def pfile(name):
    slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") or "learner"
    return DATA_DIR / f"{slug}.json"


def load_progress(name):
    p = default_progress()
    f = pfile(name)
    if f.exists():
        try:
            p.update(json.loads(f.read_text(encoding="utf-8")))
        except Exception:
            pass
    return p


def save_progress():
    try:
        pfile(st.session_state.user).write_text(json.dumps(st.session_state.prog, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception:
        pass  # read-only hosting: progress lives for the session


def add_xp(n):
    p = st.session_state.prog
    today = date.today()
    if p["last_day"] != today.isoformat():
        y = (today - timedelta(days=1)).isoformat()
        p["streak"] = p["streak"] + 1 if p["last_day"] == y else 1
        p["last_day"] = today.isoformat()
    p["xp"] += n
    save_progress()


def level(xp):
    return xp // 100 + 1


# ---------------------------------------------------------------- audio
@st.cache_data(show_spinner=False)
def tts(text):
    from gtts import gTTS

    buf = io.BytesIO()
    gTTS(text=text, lang="kn").write_to_fp(buf)
    return buf.getvalue()


def audio_player(items, key):
    labels = [f"{i['kn']}  —  {i['en']}" for i in items]
    c1, c2 = st.columns([3, 1])
    pick = c1.selectbox("🔊 Listen to pronunciation", labels, key=f"sel_{key}")
    if c2.button("Play", key=f"play_{key}"):
        try:
            st.audio(tts(items[labels.index(pick)]["kn"]), format="audio/mp3")
        except Exception:
            st.warning("Audio needs an internet connection (gTTS). Check your connection and try again.")


def navigate(page):
    st.session_state.page = page


# ---------------------------------------------------------------- session setup
st.session_state.setdefault("page", "Home")
st.session_state.setdefault("quiz", None)
st.session_state.setdefault("fc", {"cur": None, "flip": False})

with st.sidebar:
    st.markdown("## 📘 NammaKannada")
    st.caption("Your Kannada Learning Companion")
    st.markdown("**MAIN MENU**")
    st.radio("Menu", PAGES, key="page", label_visibility="collapsed")
    st.markdown("---")
    st.markdown("### 🧑‍🎓 Learner Profile")
    name = st.text_input("Your name", value="Learner").strip() or "Learner"
    if st.session_state.get("user") != name:
        st.session_state.user = name
        st.session_state.prog = load_progress(name)
    prog = st.session_state.prog
    st.metric("⭐ XP", prog["xp"], help=f"Level {level(prog['xp'])}")
    st.caption(f"Level {level(prog['xp'])} • 🔥 {prog['streak']} day streak")
    st.caption("Made with ❤️ to celebrate Kannada")

page = st.session_state.page
prog = st.session_state.prog


def hero(title, sub):
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{sub}</p></div>', unsafe_allow_html=True)


# ---------------------------------------------------------------- HOME
if page == "Home":
    hero(f"ನಮಸ್ಕಾರ, {name}! 👋", "Learn Kannada step by step: lessons, audio, flashcards and quizzes with Hindi and English meanings.")
    c = st.columns(4)
    c[0].metric("⭐ Total XP", prog["xp"])
    c[1].metric("🏅 Level", level(prog["xp"]))
    c[2].metric("🔥 Streak", f"{prog['streak']} days")
    c[3].metric("📖 Lessons done", f"{len(prog['lessons_done'])}/{len(LESSONS)}")

    wod = ALL_ITEMS[date.today().toordinal() % len(ALL_ITEMS)]
    st.markdown("### 🌟 Word of the Day")
    st.markdown(
        f'<div class="card"><div class="kn">{wod["kn"]}</div><div class="tr">{wod["tr"]}</div>'
        f'<b>English:</b> {wod["en"]} &nbsp;|&nbsp; <b>हिन्दी:</b> {wod["hi"]}</div>',
        unsafe_allow_html=True,
    )
    audio_player([wod], "wod")

    st.markdown("### 🚀 Start now")
    b = st.columns(4)
    b[0].button("📖 Learn", on_click=navigate, args=("Learn Kannada",), use_container_width=True)
    b[1].button("🗂️ Flashcards", on_click=navigate, args=("Flashcards",), use_container_width=True)
    b[2].button("🎯 Quiz", on_click=navigate, args=("Practice Quiz",), use_container_width=True)
    b[3].button("💬 Phrasebook", on_click=navigate, args=("Phrasebook",), use_container_width=True)
    st.info("Tip: study a little every day. A streak gives you consistency, and consistency builds fluency.")

# ---------------------------------------------------------------- LEARN
elif page == "Learn Kannada":
    hero("📖 Learn Kannada", "Four beginner lessons with script, pronunciation, English and Hindi meanings.")
    for l in LESSONS:
        done = l["id"] in prog["lessons_done"]
        with st.expander(f"{l['icon']} Lesson {l['id']:02d} — {l['title']} {'✅' if done else ''}", expanded=(l["id"] == 1)):
            st.info(f"💡 {l['tip']}")
            df = pd.DataFrame(l["words"])[["kn", "tr", "en", "hi"]]
            df.columns = ["ಕನ್ನಡ", "Pronunciation", "English", "हिन्दी"]
            st.dataframe(df, hide_index=True, use_container_width=True)
            audio_player(l["words"], f"l{l['id']}")
            c1, c2 = st.columns(2)
            if c1.button("✅ Mark lesson complete (+20 XP)", key=f"done{l['id']}", disabled=done):
                prog["lessons_done"].append(l["id"])
                add_xp(20)
                st.rerun()
            if c2.button("🎯 Quiz me on this lesson", key=f"lq{l['id']}"):
                st.session_state.quiz_scope = f"Lesson {l['id']}"
                st.session_state.quiz = None
                navigate("Practice Quiz")
                st.rerun()

# ---------------------------------------------------------------- PHRASEBOOK
elif page == "Phrasebook":
    hero("💬 Phrasebook", "Useful everyday phrases for travel, food, shopping and emergencies.")
    cats = ["All"] + sorted({p["cat"] for p in PHRASES})
    c1, c2 = st.columns([2, 1])
    q = c1.text_input("🔍 Search (Kannada, English, Hindi or pronunciation)").strip().lower()
    cat = c2.selectbox("Category", cats)
    shown = [
        p for p in PHRASES
        if (cat == "All" or p["cat"] == cat)
        and (not q or q in (p["kn"] + p["tr"] + p["en"] + p["hi"]).lower())
    ]
    st.caption(f"{len(shown)} phrase(s)")
    for p in shown:
        st.markdown(
            f'<div class="card"><span class="badge">{p["cat"]}</span><div class="kn">{p["kn"]}</div>'
            f'<div class="tr">{p["tr"]}</div><b>{p["en"]}</b> &nbsp;|&nbsp; {p["hi"]}</div>',
            unsafe_allow_html=True,
        )
    if shown:
        audio_player(shown, "phr")
    else:
        st.warning("No phrases found. Try another word.")

# ---------------------------------------------------------------- FLASHCARDS
elif page == "Flashcards":
    hero("🗂️ Flashcards", "Spaced repetition: cards you miss come back more often.")
    scope = st.selectbox("Deck", ["All"] + [f"Lesson {l['id']} — {l['title']}" for l in LESSONS] + ["Phrasebook"])
    if scope == "All":
        deck = ALL_ITEMS
    elif scope == "Phrasebook":
        deck = PHRASES
    else:
        deck = LESSONS[int(scope.split()[1]) - 1]["words"]
    fc = st.session_state.fc
    box = lambda it: prog["cards"].get(it["kn"], 0)
    mastered = sum(1 for it in deck if box(it) >= 3)
    st.progress(mastered / len(deck), text=f"Mastered {mastered}/{len(deck)} cards")

    if fc["cur"] is None or fc["cur"] not in [d["kn"] for d in deck]:
        low = min(box(d) for d in deck)
        fc["cur"] = random.choice([d for d in deck if box(d) == low])["kn"]
        fc["flip"] = False
    card = next(d for d in deck if d["kn"] == fc["cur"])

    if not fc["flip"]:
        st.markdown(f'<div class="flash"><div class="big-kn">{card["kn"]}</div><p>What does this mean?</p></div>', unsafe_allow_html=True)
        if st.button("🔄 Flip card", use_container_width=True):
            fc["flip"] = True
            st.rerun()
    else:
        st.markdown(
            f'<div class="flash"><div class="big-kn">{card["kn"]}</div><div class="tr">{card["tr"]}</div>'
            f'<h3>{card["en"]}</h3><h3>{card["hi"]}</h3></div>',
            unsafe_allow_html=True,
        )
        c1, c2 = st.columns(2)

        def rate(known):
            prog["cards"][card["kn"]] = min(box(card) + 1, 4) if known else 0
            add_xp(2 if known else 0)
            fc["cur"], fc["flip"] = None, False

        c1.button("😓 Again", on_click=rate, args=(False,), use_container_width=True)
        c2.button("😎 I knew it (+2 XP)", on_click=rate, args=(True,), use_container_width=True)
    audio_player([card], "fc")

# ---------------------------------------------------------------- QUIZ
elif page == "Practice Quiz":
    hero("🎯 Kannada Practice Quiz", "Test your Kannada vocabulary. Every question is randomised.")
    MODES = {"Kannada → English": ("kn", "en"), "English → Kannada": ("en", "kn"), "Kannada → Hindi": ("kn", "hi")}

    def label(x, tgt):
        return f"{x['kn']} ({x['tr']})" if tgt == "kn" else x[tgt]

    def build(pool, mode, n):
        src, tgt = MODES[mode]
        qs = []
        for it in random.sample(pool, min(n, len(pool))):
            ans = label(it, tgt)
            others = list({label(x, tgt) for x in pool if label(x, tgt) != ans})
            opts = random.sample(others, 3) + [ans]
            random.shuffle(opts)
            if tgt == "hi":
                text = f"What is the Hindi meaning of '{it['kn']}'?"
            elif src == "kn":
                text = f"What does '{it['kn']}' mean?"
            else:
                text = f"How do you say '{it['en']}' in Kannada?"
            qs.append({"q": text, "options": opts, "answer": ans, "kn": it["kn"], "tr": it["tr"], "en": it["en"]})
        return qs

    qz = st.session_state.quiz
    if qz is None:
        scopes = ["All"] + [f"Lesson {l['id']}" for l in LESSONS] + ["Phrasebook"]
        default = scopes.index(st.session_state.pop("quiz_scope", "All"))
        c1, c2, c3 = st.columns(3)
        mode = c1.selectbox("Mode", list(MODES))
        scope = c2.selectbox("Topic", scopes, index=default)
        n = c3.slider("Questions", 5, 20, 10)
        if scope == "All":
            pool = ALL_ITEMS
        elif scope == "Phrasebook":
            pool = PHRASES
        else:
            pool = LESSONS[int(scope.split()[1]) - 1]["words"]
        if len(pool) < 4:
            st.error("Not enough words in this topic.")
        elif st.button("▶️ Start Quiz"):
            st.session_state.quiz = {
                "id": random.randint(0, 10**9), "qs": build(pool, mode, n), "i": 0, "score": 0,
                "checked": False, "last": None, "log": [], "saved": False, "mode": mode, "scope": scope,
            }
            st.rerun()
    elif qz["i"] >= len(qz["qs"]):
        total = len(qz["qs"])
        pct = round(100 * qz["score"] / total)
        if not qz["saved"]:
            xp = qz["score"] * 5 + (20 if qz["score"] == total else 0)
            prog["history"].append({"date": date.today().isoformat(), "score": qz["score"], "total": total, "mode": qz["mode"], "scope": qz["scope"]})
            add_xp(xp)
            qz["saved"], qz["xp"] = True, xp
        st.markdown("## 🏁 Quiz complete!")
        st.metric("Score", f"{qz['score']}/{total}", f"{pct}%")
        st.success(f"You earned +{qz['xp']} XP!") if pct >= 60 else st.info(f"+{qz['xp']} XP. Review the lessons and try again!")
        if pct == 100:
            st.balloons()
        rev = pd.DataFrame(qz["log"])
        rev.columns = ["Question", "Your answer", "Correct answer", "Result"]
        st.dataframe(rev, hide_index=True, use_container_width=True)
        c1, c2 = st.columns(2)
        if c1.button("🔁 New quiz"):
            st.session_state.quiz = None
            st.rerun()
        c2.button("📖 Back to lessons", on_click=navigate, args=("Learn Kannada",))
    else:
        i, q = qz["i"], qz["qs"][qz["i"]]
        st.progress(i / len(qz["qs"]), text=f"Question {i + 1} of {len(qz['qs'])}   •   Score {qz['score']}")
        st.markdown(f"### {q['q']}")
        choice = st.radio("Choose an answer", q["options"], index=None, key=f"r{qz['id']}_{i}", disabled=qz["checked"], label_visibility="collapsed")
        if not qz["checked"]:
            if st.button("Check Answer"):
                if choice is None:
                    st.warning("Please select an answer first.")
                else:
                    ok = choice == q["answer"]
                    qz["score"] += ok
                    qz["checked"], qz["last"] = True, ok
                    qz["log"].append({"q": q["q"], "your": choice, "correct": q["answer"], "res": "✅" if ok else "❌"})
                    st.rerun()
        else:
            if qz["last"]:
                st.success("✅ Correct! Shabash!")
            else:
                st.error(f"❌ Not quite. Correct answer: **{q['answer']}**")
            st.caption(f"{q['kn']} ({q['tr']}) = {q['en']}")
            if st.button("Next ➡️" if i + 1 < len(qz["qs"]) else "See results 🏁"):
                qz["i"] += 1
                qz["checked"] = False
                st.rerun()
        if st.button("✖ Quit quiz", key="quit"):
            st.session_state.quiz = None
            st.rerun()

# ---------------------------------------------------------------- PROGRESS
elif page == "My Progress":
    hero("📊 My Progress", f"Keep going, {name}!")
    c = st.columns(4)
    c[0].metric("⭐ XP", prog["xp"])
    c[1].metric("🏅 Level", level(prog["xp"]))
    c[2].metric("🔥 Streak", prog["streak"])
    c[3].metric("🧠 Cards mastered", sum(1 for v in prog["cards"].values() if v >= 3))
    st.progress(prog["xp"] % 100 / 100, text=f"{100 - prog['xp'] % 100} XP to level {level(prog['xp']) + 1}")

    st.markdown("### 🏆 Badges")
    h = prog["history"]
    badges = [
        ("🌱 First Steps", prog["xp"] > 0),
        ("📖 Lesson Learner", len(prog["lessons_done"]) >= 1),
        ("🎓 Course Complete", len(prog["lessons_done"]) == len(LESSONS)),
        ("🎯 Perfect Quiz", any(x["score"] == x["total"] for x in h)),
        ("🔥 3-Day Streak", prog["streak"] >= 3),
        ("🧠 Card Master", sum(1 for v in prog["cards"].values() if v >= 3) >= 10),
    ]
    st.markdown("".join(f'<span class="badge {"" if ok else "off"}">{b}</span>' for b, ok in badges), unsafe_allow_html=True)

    st.markdown("### 📈 Quiz history")
    if h:
        df = pd.DataFrame(h)
        df["Accuracy %"] = (100 * df["score"] / df["total"]).round()
        st.line_chart(df["Accuracy %"])
        st.dataframe(df.iloc[::-1], hide_index=True, use_container_width=True)
    else:
        st.info("No quizzes taken yet. Take one to see your progress here.")
    if st.button("🗑️ Reset my progress"):
        st.session_state.prog = default_progress()
        save_progress()
        st.rerun()

# ---------------------------------------------------------------- ABOUT
else:
    hero("ℹ️ About NammaKannada", "An independent educational project to make learning Kannada easy and fun.")
    st.markdown(
        """
**Features:** structured lessons • Kannada script + pronunciation + English + Hindi • text-to-speech audio •
phrasebook with search • spaced-repetition flashcards • randomised quizzes with 3 modes • XP, levels, streaks and badges •
per-learner saved progress.

**Built with:** Python, Streamlit, pandas, gTTS.

**Roadmap:** Kannada alphabet (ಅ–ಹ) writing practice, speech recognition, more lessons, leaderboard, mobile app.

**Why it matters:** Kannada is spoken by 60+ million people. Migrants, students and travellers in Karnataka deserve
a simple, free way to connect with the language.
"""
    )

st.markdown('<div class="foot">NammaKannada © 2026 | Learn Kannada. Connect with Karnataka. ❤️</div>', unsafe_allow_html=True)
