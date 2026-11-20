# DSA Tracker
A small web page for logging the data structures and algorithms problems I solve, built with Flask and SQLite.
I use it to keep track of what I've practiced and soon, to schedule reviews of old problems so I don't forget them.

## Status
Work in progress. 
Planned next: edit and delete, a spaced-repetition review list, a stats page, tests, and a live demo

## Features so far
- add a solved problem with a title, topic and difficulty
- the date solved is saved automatically
- newest problems are shown first
- server-side input validation (required title, length limit, topic and difficulty must come from the allowed lists)
- pages are rendered with Jinja templates, which escape user input so HTML types into a form is shown as text

## Tech
- Python 3, Flask
- SQLite (through Python's built in 'sqlite3' module)
- Jinja2 template

## How to run
1. install python 3 and flask: `python -m pip install flask`
2. clone the repo and open the folder
3. run `python app.py`
4. open http://127.0.0.1:5000 in your browser

the database file 'tracker.db' is created automatically on the first run.
