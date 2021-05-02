from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() :
    return "index"

@app.route("/pending")
def pending() :
    return "Pending"

@app.route("/confirm")
def confirm() :
    return "Confirm"

@app.route("/reject")
def reject() :
    return "Reject"

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)