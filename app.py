from flask import Flask, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

def db():
    conn = sqlite3.connect("tracker.db")
    conn.execute("CREATE TABLE IF NOT EXISTS problems (id INTEGER PRIMARY KEY, title TEXT, topic TEXT, difficulty TEXT, date_solved TEXT)")
    return conn

@app.route("/", methods=["GET", "POST"])
def home():
    conn = db()
    if request.method == "POST":
        conn.execute("INSERT INTO problems (title, topic, difficulty, date_solved) VALUES (?, ?, ?, ?)",
                     (request.form["title"], request.form["topic"], request.form["difficulty"], date.today().isoformat()))
        conn.commit()
        return redirect("/")
    rows = conn.execute("SELECT title, topic, difficulty, date_solved FROM problems").fetchall()
    items = "".join(f"<li>{t} | {tp} | {d} | {ds}</li>" for t, tp, d, ds in rows)
    return f"""
        <form method="post">
            <input name="title" placeholder="Problem title" required>
            <input name="topic" placeholder="Topic (e.g. Array)" required>
            <select name="difficulty"><option>Easy</option><option>Medium</option><option>Hard</option></select>
            <button>Add</button>
        </form>
        <ul>{items}</ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
