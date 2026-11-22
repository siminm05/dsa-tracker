from flask import Flask, request, redirect, render_template, flash, abort
from datetime import date
import db

app = Flask(__name__)
app.secret_key = "dev-only-change-me"
db.init_db()

TOPICS = ["Array", "String", "Hash Map", "Linked List", "Stack/Queue",
          "Tree", "Graph", "DP", "Sorting", "Binary Search", "Other"]
DIFFICULTIES = ["Easy", "Medium", "Hard"]

def validate(form):
    data = {
        "title": form.get("title", "").strip(),
        "topic": form.get("topic", ""),
        "difficulty": form.get("difficulty", ""),
    }
    errors = []
    if not data["title"]:
        errors.append("Title is required.")
    elif len(data["title"]) > 100:
        errors.append("Title must be 100 characters or fewer.")
    if data["topic"] not in TOPICS:
        errors.append("Pick a topic from the list.")
    if data["difficulty"] not in DIFFICULTIES:
        errors.append("Pick a difficulty from the list.")
    return data, errors

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data, errors = validate(request.form)
        if errors:
            for e in errors:
                flash(e)
        else:
            db.execute("INSERT INTO problems (title, topic, difficulty, date_solved) VALUES (?, ?, ?, ?)",
                       (data["title"], data["topic"], data["difficulty"], date.today().isoformat()))
            flash("Problem added!")
        return redirect("/")
    rows = db.query("SELECT id, title, topic, difficulty, date_solved FROM problems ORDER BY id DESC")
    return render_template("index.html", problems=rows, topics=TOPICS, difficulties=DIFFICULTIES)

@app.route("/delete/<int:problem_id>", methods=["POST"])
def delete(problem_id):
    db.execute("DELETE FROM problems WHERE id = ?", (problem_id,))
    flash("Problem deleted.")
    return redirect("/")

@app.route("/edit/<int:problem_id>", methods=["GET", "POST"])
def edit(problem_id):
    rows = db.query("SELECT id, title, topic, difficulty FROM problems WHERE id = ?", (problem_id,))
    if not rows:
        abort(404)
    problem = rows[0]
    if request.method == "POST":
        data, errors = validate(request.form)
        if errors:
            for e in errors:
                flash(e)
        else:
            db.execute("UPDATE problems SET title = ?, topic = ?, difficulty = ? WHERE id = ?",
                       (data["title"], data["topic"], data["difficulty"], problem_id))
            flash("Problem updated.")
            return redirect("/")
    return render_template("edit.html", problem=problem, topics=TOPICS, difficulties=DIFFICULTIES)

if __name__ == "__main__":
    app.run(debug=True)