# DSA Tracker
A small web app for logging the data structures and algorithms problems I solve, built with Flask and SQLite.
I use it to keep track of what I've practiced and, soon, to schedule reviews of old problems so I don't forget them.

## Status
Work in progress.
Planned next: a spaced-repetition review list, tests, and a live demo.

## Features so far
- Add a solved problem with a title, topic and difficulty
- The date solved is saved automatically
- Edit and delete problems
- Newest problems are shown first
- Server-side input validation (required title, length limit, topic and difficulty must come from the allowed lists)
- Pages are rendered with Jinja templates, which escape user input so HTML typed into a form is shown as text

## Tech
- Python 3, Flask
- SQLite (through Python's built-in `sqlite3` module)
- Jinja2 templates

## Project structure
```
app.py          routes and input validation
db.py           database helpers (query, execute, init_db)
templates/      HTML templates (index.html, edit.html)
```

## How to run
1. Install Python 3 and Flask: `python -m pip install flask`
2. Clone the repo: `git clone https://github.com/siminm05/dsa-tracker.git`
3. Open the folder and run `python app.py`
4. Open http://127.0.0.1:5000 in your browser

The database file `tracker.db` is created automatically on the first run.