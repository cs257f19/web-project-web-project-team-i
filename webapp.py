#!/usr/bin/env python3
'''
    webapp.py
'''
import flask
from flask import Flask, flash, redirect, render_template, request, url_for
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
    year = request.form['year']
    categories = ["picture","actor","actress","director"]

    if int(year) < 1927 or int(year) > 2018:
        title =  'The year ' + year + ' is out of range. Please go back and type in again.'
        return render_template('result.html', winners=[], year=year, title=title)
    else:
        for category in categories:
            result = ds.get_winner(connection, int(year), category)
            film = result[0][0]
            if category != "picture":
                person = result[0][1]
            else:
                person = ""
            winners.append({"award":category, "film":film, "person":person})

            title = year + ' Oscar Winners'

        return render_template('result.html',
                            winners=winners,
                            year=year,
                            title=title)


@app.route('/pictures')
def pictures():
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)


    year = 0
    category = "picture"
    pictures = ds.get_winner(connection, year, category)
    return render_template('pictures.html', pictures=pictures)

@app.route('/actors')
def actors():
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)


    year = 0
    category = "actor"
    actors = ds.get_winner(connection, year, category)

    return render_template('actors.html', actors=actors)

@app.route('/actresses')
def actresses():
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)


    year = 0
    category = "actress"
    actresses = ds.get_winner(connection, year, category)

    return render_template('actresses.html', actresses=actresses)

@app.route('/directors')
def directors():
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)


    year = 0
    category = "director"
    directors = ds.get_winner(connection, year, category)
    return render_template('directors.html', directors=directors)



@app.route('/trends')
def trends():
    return render_template('trends.html')


@app.route('/about_oscars')
def about_oscars():
    return render_template('about-oscars.html')

@app.route('/winners2020')
def winners2020():
    return render_template('winners2020.html')

@app.route('/about_data')
def about_data():
    return render_template('about-data.html')

@app.route('/terms_of_use')
def terms_of_use():
    return render_template('terms.html')




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
