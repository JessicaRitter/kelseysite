from jinja2 import StrictUndefined
# from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, jsonify, render_template, redirect, request, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
# import os


app = Flask(__name__)


# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_home():
    greeting = "Hello World"
    return render_template('home.html')















if __name__ == '__main__':
    app.debug = True
    #no caching for templates
    app.jinja_env.auto_reload = app.debug 

    # connect_to_db(app)

    # DebugToolbarExtension(app)

    app.run(host='0.0.0.0')