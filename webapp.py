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
    winners = []
    # picCategory = "picture"
    # actorCategory = "actor"
    # actressCategory = "actress"
    # directorCategory = "director"
    year = request.form['year']
    categories = ["picture","actor","actress","director"]
    for category in categories:
        result = ds.get_winner(connection, year, category)
        film = result[0][0]
        if category != "picture":
            person = result[0][1]
        else:
            person = ""
        winners.append({"award":category, "film":film, "person":person})
    # bestPic = ds.get_by_year(connection, year, picCategory)
    # bestActor = ds.get_by_year(connection, year, actorCategory)
    # bestActress = ds.get_by_year(connection, year, actressCategory)
    # bestDirector = ds.get_by_year(connection, year, directorCategory)

    return render_template('result.html',
                           winners=winners,
                           year=year)

@app.route('/data')
def about():
    return render_template('about-data.html')




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
