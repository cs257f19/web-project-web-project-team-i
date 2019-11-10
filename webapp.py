#!/usr/bin/env python3
'''
    webapp.py
'''
import flask
from flask import render_template
import json
import sys

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about-data.html')

@app.route('/actor/<year>')
def actor():
    return render_template('pages/actor.html', year=year)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
