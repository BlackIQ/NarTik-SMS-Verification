from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() :
    render_template("index.html")

@app.route("pending")
def pending() :
    render_template("pending")

@app.route("confirm")
def confirm() :
    render_template("confirm.html")

@app.route("reject")
def reject() :
    render_template("reject.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)