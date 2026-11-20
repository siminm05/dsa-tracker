from flask import Flask, request, redirect
from datetime import date
import db

app = Flask(__name__)
db.init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        db.execute("INSERT INTO problems (title, topic, difficulty, date_solved) VALUES (?, ?, ?, ?)",
                   (request.form["title"], request.form["topic"], request.form["difficulty"], date.today().isoformat()))
        return redirect("/")
    rows = db.query("SELECT title, topic, difficulty, date_solved FROM problems ORDER BY id DESC")
    items = "".join(f"<li>{r['title']} | {r['topic']} | {r['difficulty']} | {r['date_solved']}</li>" for r in rows)
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