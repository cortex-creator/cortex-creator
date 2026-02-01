# Jobbot

Offline-friendly job application helper with resume parsing, scraping, matching, and a FastAPI backend.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

## Project Structure

```
jobbot/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── matcher.py
│   ├── resume_parser.py
│   ├── cover_letter.py
│   ├── scrapers/
│   │   ├── greenhouse.py
│   │   ├── lever.py
│   │   └── rss.py
│   └── routes/
│       ├── jobs.py
│       ├── resume.py
│       └── applications.py
├── data/
│   └── jobbot.db
├── requirements.txt
└── README.md
```
