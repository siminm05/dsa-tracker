from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def db():
    conn = sqlite3.connect("tracker.db")
    conn.execute("CREATE TABLE IF NOT EXISTS problems (id INTEGER PRIMARY KEY, title TEXT, difficulty TEXT)")
    return conn

@app.route("/", methods=["GET", "POST"])
def home():
    conn = db()
    if request.method == "POST":
        conn.execute("INSERT INTO problems (title, difficulty) VALUES (?, ?)",
                     (request.form["title"], request.form["difficulty"]))
        conn.commit()
        return redirect("/")
    rows = conn.execute("SELECT title, difficulty FROM problems").fetchall()
    items = "".join(f"<li>{t} ({d})</li>" for t, d in rows)
    return f"""
        <form method="post">
            <input name="title" placeholder="Problem title" required>
            <select name="difficulty"><option>Easy</option><option>Medium</option><option>Hard</option></select>
            <button>Add</button>
        </form>
        <ul>{items}</ul>
    """

if __name__ == "__main__":
    app.run(debug=True)