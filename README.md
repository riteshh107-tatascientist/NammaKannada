# 📘 NammaKannada — Your Kannada Learning Companion

NammaKannada is a free, interactive web app that helps beginners learn **Kannada** with Kannada script, pronunciation, and **English and Hindi** meanings. It includes lessons, audio, flashcards, quizzes, and progress tracking.

> *Learn Kannada. Connect with Karnataka.* ❤️

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔤 **Alphabet** | Kannada vowels and consonants with pronunciation and audio |
| 📖 **Lessons** | 4 beginner lessons: Greetings, Basic Vocabulary, Numbers, Introducing Yourself |
| 🔊 **Audio** | Listen to Kannada pronunciation (text-to-speech) |
| 💬 **Phrasebook** | Everyday phrases for shopping, food, travel, conversation and emergencies, with search |
| 🗂️ **Flashcards** | Spaced-repetition cards: words you miss come back more often |
| 🎯 **Practice Quiz** | Randomised questions in 3 modes (Kannada→English, English→Kannada, Kannada→Hindi) |
| 📊 **Progress** | XP, levels, daily streak, badges and quiz history chart |
| 🌟 **Word of the Day** | A new word every day on the home page |
| 👤 **Learner profiles** | Progress is saved separately for each learner name |

---

## 🚀 Getting Started

### Requirements
- Python 3.9 or newer
- Internet connection (needed only for audio)

### Install and run
```bash
# 1. Go to the project folder
cd nammakannada

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the app
streamlit run Kannada_app.py
```
The app opens at `http://localhost:8501`.

---

## 📁 Project Structure

```
nammakannada/
├── Kannada_app.py             # Main Streamlit app (all pages and logic)
├── data.py              # Lessons, words and phrases (edit this to add content)
├── requirements.txt     # Python dependencies
├── .streamlit/
│   └── config.toml      # Light theme settings
└── user_data/           # Auto-created: saved learner progress (JSON)
```

---

## ➕ Adding New Content

Open `data.py`.

**Add a word to a lesson:**
```python
w("ಕನ್ನಡ", "Kannada", "Kannada (language)", "कन्नड़"),
```
Format: `w(kannada_script, pronunciation, english, hindi)`

**Add a new lesson:** copy an existing block inside `LESSONS`, give it a new `id`, `icon`, `title`, `tip` and `words`.

**Add a phrase:** add a line to `PHRASES` with a category such as `"🍽️ Food"`.

The quiz, flashcards and search use the new content automatically.

---

## ☁️ Deploy for Free (Streamlit Community Cloud)

1. Push this folder to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, select your repo, and set the main file to `Kannada_app.py`.
4. Click **Deploy** and share your public link.

> On Streamlit Cloud, saved progress may reset when the app restarts, because the hosting disk is temporary. For permanent storage, connect a database later.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **pandas** (tables and charts)
- **gTTS** (Kannada text-to-speech)

---

## 🗺️ Roadmap

- [ ] Kannada alphabet (ಅ–ಹ) with audio and writing practice
- [ ] More lessons (family, food, travel, days and months)
- [ ] Speech recognition for pronunciation practice
- [ ] Leaderboard
- [ ] Database for permanent cloud progress

---

## ⚠️ Note on Content

Kannada and Hindi content is written for beginners. Native speakers are welcome to review and improve it. Open an issue or a pull request.

---

## 📄 License

An independent educational project. Free to use for learning. Add your preferred license (for example MIT) before distributing.

---

**NammaKannada © 2026** — Made with ❤️ to celebrate Kannada.
