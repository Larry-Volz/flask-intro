from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def add_args():
    """ return sum of two numbers acquired through a GET posting """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.route('/sub')
def sub_args():
    """ return difference of two numbers acquired through a GET posting """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route('/mult')
def mult_args():
    """ return product of two numbers acquired through a GET posting """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route('/div')
def div_args():
    """ return quotient of two numbers acquired through a GET posting """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))