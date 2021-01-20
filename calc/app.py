from flask import Flask, request
from operations import *

app = Flask(__name__)

functions = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<func>")
def do_math(func):
    """Perform math calculations on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = functions[func](a, b)

    return str(result)