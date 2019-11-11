#!/usr/bin/env python3
'''
    webapp.py
'''
import flask
from flask import render_template
import backend.datasource
import json
import sys

app = flask.Flask(__name__)
ds = backend.datasource.DataSource()

user = 'kuritar'
password = 'lamp977python'
connection = ds.connect(user, password)

category = "picture"
year = 2000


@app.route('/')
def homepage():
    return render_template('index.html')

# @app.route('/about-data')
# def about():
#     return render_template('pages/about-data.html')

# @app.route('/actor/<year>')
# def actor():
#     return render_template('pages/actor.html', year=year)


@app.route('/result')
def picture():
    bestPic = ds.get_by_year(connection, year, category)

    return render_template('result.html',
                           bestPic=bestPic)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
