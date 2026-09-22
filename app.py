from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>메인페이지</h1>"

@app.route("/about")
def about():
    return "<h1>소개페이지</h1>"

@app.route("/test/<text>")
def route_test(text):
    return f"<h1>{text}</h1>"

@app.route("/age/<num>")
def age_any(num):
    return f"<h1>{num} 살 - 타입은 {type(num).__name__}</h1>"

@app.route("/age2/<int:num>")
def age_int(num):
    return f"<h1>{num} 살 - 타입은 {type(num).__name__}</h1>"

@app.route("/hi/<name>")
def hi(name):
    return render_template("index.html", name=name)