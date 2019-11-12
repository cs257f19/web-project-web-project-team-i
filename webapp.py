#!/usr/bin/env python3
'''
    webapp.py
'''
import flask
from flask import Flask, render_template, request
import backend.datasource
import json
import sys


app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    ds = backend.datasource.DataSource()

    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)
    picCategory = "picture"
    actorCategory = "actor"
    actressCategory = "actress"
    directorCategory = "director"
    year = request.form['year']
    bestPic = ds.get_by_year(connection, year, picCategory)
    bestActor = ds.get_by_year(connection, year, actorCategory)
    bestActress = ds.get_by_year(connection, year, actressCategory)
    bestDirector = ds.get_by_year(connection, year, directorCategory)

    return render_template('result.html',
                           bestPic=bestPic,
                           bestActor=bestActor,
                           bestActress=bestActress,
                           bestDirector=bestDirector,
                           year=year)

# @app.route('/about-data')
# def about():
#     return render_template('pages/about-data.html')

# @app.route('/actor/<year>')
# def actor():
#     return render_template('pages/actor.html', year=year)


@app.route('/result')
def picture():

    ds = backend.datasource.DataSource()

    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)
    category = "picture"
    year = 2000
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
