from flask import Flask, render_template


app = Flask(__name__)

STUDENT = {
    "name": "안세호",
    "student_id": "23013283",
}

HOBBIES = [
    "기타 연습",
    "수영",
    "헬스",
]


@app.route("/")
def introduce():
    return render_template("introduce.html", student=STUDENT)


@app.route("/profile")
def profile():
    return render_template("profile.html", student=STUDENT, hobbies=HOBBIES)


@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", student=STUDENT, name=name)


if __name__ == "__main__":
    app.run(debug=True)
