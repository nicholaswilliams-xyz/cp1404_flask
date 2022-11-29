"""
Use flask to create a basic webpage, with routes and functions.
Practical repo: https://github.com/CP1404/Practicals/tree/master/prac_10
"""


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<fahrenheit>')
def f(fahrenheit=0.0):
    try:
        return f"{fahrenheit}°F = {convert_fahrenheit_to_celsius(float(fahrenheit)):0.4f}°C"
    except TypeError:
        return "Numbers only"


@app.route('/c')
@app.route('/c/<celsius>')
def c(celsius=0.0):
    try:
        return f"{celsius}°C = {convert_celsius_to_fahrenheit(float(celsius)):0.2f}°F"
    except TypeError:
        return "Numbers only"


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
