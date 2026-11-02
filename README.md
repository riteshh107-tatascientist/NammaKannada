# NammaKannada — Your Kannada Learning Companion

A beginner-friendly Kannada learning app with lessons, a searchable phrasebook, pronunciation audio, flashcards, quizzes, and learner progress.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run Kannada_app.py
```

## Deploy on Streamlit Community Cloud

1. Upload all files in this folder to the root of a GitHub repository.
2. In Streamlit Community Cloud, select that repository and branch.
3. Set **Main file path** to `Kannada_app.py`.
4. Deploy.

Important: keep `Kannada_app.py` and `data.py` together in the repository root. The app imports `ALL_ITEMS`, `LESSONS`, and `PHRASES` from `data.py`.

Progress is stored in local JSON files under `user_data/`. On hosted platforms with ephemeral storage, it may not persist permanently.
