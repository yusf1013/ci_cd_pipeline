from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return {
        'msg': 'Hello World!',
        'app_version': '4'
    }


@app.route('/add/<a>/<b>')
def add_route(a, b):
    return {
        'sum': add(a, b)
    }


@app.route('/subtract/<a>/<b>')
def add_route2(a, b):
    return {
        'difference': subtract(a, b)
    }


@app.route('/multiply/<a>/<b>')
def add_route3(a, b):
    return {
        'product': multiply(a, b)
    }


@app.route('/divide/<a>/<b>')
def add_route4(a, b):
    return {
        'ratio': divide(a, b)
    }

# Input can be both strings and digits

def add(a, b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a + b


def subtract(a, b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a - b


def multiply(a, b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a * b


def divide(a, b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)

    if b == 0:
        return "Division by zero"

    return a / b


if __name__ == "__main__":
    app.run()
