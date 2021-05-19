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
def send():
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
        

@app.route("/confirm", methods = ["GET", "POST"])
def confirm():
    if "phone" in request.args:
        phone = request.args["phone"]

        params = {
            'sender': '1000596446',
            'receptor': phone,
            'message': "کاربر گرامی، شما در نارتیک تایید شده اید."
        }

        response = api.sms_send(params)

        return redirect("http://office.narbon.ir:4488/NarFirm/admin")

@app.route("/reject", methods = ["GET", "POST"])
def reject():
    if "phone" in request.args:
        phone = request.args["phone"]

        params = {
            'sender': '1000596446',
            'receptor': phone,
            'message': "کاربر گرامی، شما در نارتیک تایید نشده اید."
        }

        response = api.sms_send(params)

        return redirect("http://office.narbon.ir:4488/NarFirm/admin")

@app.route("/pending", methods = ["GET", "POST"])
def pending():
    if "phone" in request.args:
        phone = request.args["phone"]

        params = {
            'sender': '1000596446',
            'receptor': phone,
            'message': "کاربر گرامی، شما در نارتیک ثبت شده اید."
        }

        response = api.sms_send(params)

        return redirect("http://office.narbon.ir:4488/NarFirm/admin")

@app.route("/sent", methods = ["GET", "POST"])
def sent():
    if "phone" in request.args:
        phone = request.args["phone"]

        params = {
            'sender': '1000596446',
            'receptor': request.args["phone"],
            'message': "کاربر گرامی، تیکت شما با موفقیت ارسال شد."
        }

        response = api.sms_send(params)

        return redirect("http://office.narbon.ir:4488/NarFirm/admin")

@app.route("/answered", methods = ["GET", "POST"])
def answered():
    if "phone" in request.args:
        phone = request.args["phone"]

        params = {
            'sender': '1000596446',
            'receptor': phone,
            'message': "کاربر گرامی، به تیکت شما پاسخ داده شد."
        }

        response = api.sms_send(params)

        return redirect("http://office.narbon.ir:4488/NarFirm/admin")

if __name__ == "__main__":
    app.run()
