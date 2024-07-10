from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def greet(name):
    return f"Hello, {name}!"

def current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

@app.route("/", methods=["GET", "POST"])
def index():
    greeting = ""
    time = current_time()
    if request.method == "POST":
        user_name = request.form.get("name")
        greeting = greet(user_name)
    return render_template("index.html", greeting=greeting, time=time)

if __name__ == "__main__":
    app.run(debug=True)
