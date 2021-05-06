from flask import Flask, request, redirect
from kavenegar import *

app = Flask(__name__)

api = KavenegarAPI('')
secret = ""

def send(code, phone, kind) :
    if code == secret :
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
        elif kind == "sent" :
            params = {
                'sender' : '1000596446',
                'receptor' : phone,
                'message' : "کاربر گرامی، تیکت شما با موفقیت ارسال شد."
            }
            response = api.sms_send(params)
        elif kind == "answered" :
            params = {
                'sender' : '1000596446',
                'receptor' : phone,
                'message' : "کاربر گرامی، به تیکت شما پاسخ داده شده است."
            }
            response = api.sms_send(params)
        else:
            return "<p>Kind is not found</p>"
    else:
        return "<p>Secret is not true</p>"

@app.route("/send", methods = ["GET", "POST"])
def index():
    if "kind" in request.args:
        if "phone" in request.args:
            if "secret" in request.args:
                send(request.args["secret"], request.args["kind"], request.args["phone"])
            else:
                return "<p>Secret is not</p>"
        else:
            return "<p>Phone is not</p>"
    else:
        return "<p>Kind is not</p>"

if __name__ == "__main__":
    app.run()