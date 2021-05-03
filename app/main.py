from flask import Flask, request, redirect
from kavenegar import *

app = Flask(__name__)

api = KavenegarAPI('')

@app.route("/")
def index() :
    return "index"

@app.route("/pending", methods = ["GET", "POST"])
def pending() :
    phone = request.args['phone']
    params = { 'sender' : '1000596446', 'receptor': phone, 'message' :"Flask Test !" }
    response = api.sms_send( params)
    return redirect("/")

@app.route("/confirm", methods=["GET", "POST"])
def confirm() :
    phone = request.args['phone']
    params = { 'sender' : '1000596446', 'receptor': phone, 'message' :"Flask Test !" }
    response = api.sms_send( params)
    return redirect("/")

@app.route("/reject", methods=["GET", "POST"])
def reject() :
    phone = request.args['phone']
    params = { 'sender' : '1000596446', 'receptor': phone, 'message' :"Flask Test !" }
    response = api.sms_send( params)
    return redirect("/")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)