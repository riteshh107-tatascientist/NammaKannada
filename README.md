# 📘 NammaKannada — Your Kannada Learning Companion

**Learn Kannada. Connect with Karnataka.** ❤️

NammaKannada is a free, interactive web application that helps beginners learn Kannada through Kannada script, pronunciation, and English and Hindi meanings.

## ✨ Features

| Feature | Description |
|---|---|
| 📖 Lessons | 4 beginner lessons: Greetings, Basic Vocabulary, Numbers and Introducing Yourself |
| 🔊 Audio | Listen to Kannada pronunciation using text-to-speech |
| 💬 Phrasebook | Everyday phrases for shopping, food, travel, conversation and emergencies |
| 🗂️ Flashcards | Spaced-repetition flashcards |
| 🎯 Practice Quiz | 3 quiz modes: Kannada → English, English → Kannada and Kannada → Hindi |
| 📊 Progress | XP, levels, daily streaks, badges and quiz history |
| 🌟 Word of the Day | Discover a new Kannada word every day |
| 👤 Learner Profiles | Save progress separately for each learner name |

## 🚀 Getting Started

### Requirements
- Python 3.10
- VS Code (recommended)
- Internet connection for audio functionality

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/NammaKannada.git
```

**2. Open the project folder**

```bash
cd NammaKannada
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the environment (Windows)**

```powershell
.venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
streamlit run app.py
```

Open your browser:

http://localhost:8501

## 📁 Project Structure

```text
NammaKannada/
│
├── app.py
├── data.py
├── requirements.txt
├── README.md
│
├── .streamlit/
│   └── config.toml
│
└── user_data/
```

## 🛠️ Technology Stack

- Python 3.10
- Streamlit
- Pandas
- gTTS (Google Text-to-Speech)
- JSON for learner progress storage

## 🎯 Project Objectives

- Promote Kannada language learning.
- Help non-Kannada speakers communicate confidently.
- Preserve regional Kannada vocabulary and expressions.
- Encourage cultural interaction.
- Make language learning accessible and interactive.

## ☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

1. Push the project to GitHub.
2. Visit https://share.streamlit.io/
3. Sign in using GitHub.
4. Select your NammaKannada repository.
5. Choose `app.py` as the main file.
6. Click Deploy.

**Note:** Local JSON-based progress storage may not persist reliably across cloud restarts. A database can be integrated for permanent storage.

## 🗺️ Future Roadmap

- [ ] Kannada alphabet learning (ಅ–ಹ).
- [ ] Kannada writing practice.
- [ ] More vocabulary and conversation lessons.
- [ ] Speech recognition for pronunciation practice.
- [ ] Community contributions for regional words.
- [ ] Regional Kannada explorer.
- [ ] Leaderboard and achievements.
- [ ] Permanent database integration.

## 🌍 Our Vision

To make Kannada learning simple, practical and accessible while celebrating Karnataka's language, culture and regional diversity.

## 🤝 Contributions

Contributions, suggestions and improvements are welcome.

Kannada speakers and learners can help improve vocabulary, pronunciation and regional expressions.

## 📄 License

Independent educational project. Add an MIT License before distributing under that license.

---

**NammaKannada © 2026**

*ಕನ್ನಡ ಕಲಿಯೋಣ, ಕರ್ನಾಟಕವನ್ನು ಸಂಪರ್ಕಿಸೋಣ!* ❤️

**Code. Create. Celebrate Kannada.**
