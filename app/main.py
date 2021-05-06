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
            pass
    else:
        pass

@app.route("/", methods = ["GET", "POST"])
def index() :
    if request.args["kind"] != None:
        if request.args["phone"] != None:
            if request.args["secret"] != None:
                send(request.args["secret"], request.args["kind"], request.args["phone"])
            else:
                return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/pending", methods = ["GET", "POST"])
def pending() :
    if request.args['secret'] != None:
        if request.args['phone'] != None:
            secret = request.args['secret']
            phone = request.args['phone']
            
            send(secret, phone, "pending")
            return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/confirm", methods=["GET", "POST"])
def confirm() :
    if request.args['secret'] != None:
        if request.args['phone'] != None:
            secret = request.args['secret']
            phone = request.args['phone']
            
            send(secret, phone, "confirm")
            return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/reject", methods=["GET", "POST"])
def reject() :
    if request.args['secret'] != None:
        if request.args['phone'] != None:
            secret = request.args['secret']
            phone = request.args['phone']
            
            send(secret, phone, "reject")
            return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/sent", methods=["GET", "POST"])
def reject():
    if request.args['secret'] != None:
        if request.args['phone'] != None:
            secret = request.args['secret']
            phone = request.args['phone']

            send(secret, phone, "sent")
            return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/answered", methods=["GET", "POST"])
def reject():
    if request.args['secret'] != None:
        if request.args['phone'] != None:
            secret = request.args['secret']
            phone = request.args['phone']

            send(secret, phone, "answered")
            return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run()