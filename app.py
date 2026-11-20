from flask import Flask, request, redirect, render_template
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
    return render_template("index.html", problems=rows)

if __name__ == "__main__":
    app.run(debug=True)