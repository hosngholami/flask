from flask import Flask, request

add_number = Flask(__name__)



@add_number.route("/sumation")
def sumation():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))

    result = num1 + num2
    return str(result)


