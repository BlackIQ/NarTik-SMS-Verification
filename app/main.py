from flask import Flask, request, redirect
from kavenegar import *

app = Flask(__name__)

api = KavenegarAPI('')

def send(secret, phone, kind) :
    if secret == "" :
        if kind == "confirm" :
            params = {
                'sender' : '1000596446',
                'receptor' : phone,
                'message' : "کاربر گرامی، شما در نارتیک تایید شده اید."
            }
            response = api.sms_send(params)
        elif kind == "reject" :
            params = {
                'sender' : '1000596446',
                'receptor' : phone,
                'message' : "کاربر گرامی، درخواست شما در سامانه نارتیک قبول نشد."
            }
            response = api.sms_send(params)
        elif kind == "pending" :
            params = {
                'sender' : '1000596446',
                'receptor' : phone,
                'message' : "کاربر گرامی، شما در صف تایید قرار گرفته اید."
            }
            response = api.sms_send(params)
        else:
            pass
    else:
        pass

@app.route("/")
def index() :
    return "index"

@app.route("/pending", methods = ["GET", "POST"])
def pending() :
    secret = request.args['secret']
    phone = request.args['phone']
    send(secret, phone, "pending")
    return redirect("/")

@app.route("/confirm", methods=["GET", "POST"])
def confirm() :
    secret = request.args['secret']
    phone = request.args['phone']
    send(secret, phone, "confirm")
    return redirect("/")

@app.route("/reject", methods=["GET", "POST"])
def reject() :
    secret = request.args['secret']
    phone = request.args['phone']
    send(secret, phone, "reject")
    return redirect("/")

if __name__ == "__main__":
    app.run()