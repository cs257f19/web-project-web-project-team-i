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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
@app.route('/about_data', methods=['POST'])
@app.route('/about_oscars', methods=['POST'])
@app.route('/about', methods=['POST'])
@app.route('/actors', methods=['POST'])
@app.route('/actresses', methods=['POST'])
@app.route('/contact_us', methods=['POST'])
@app.route('/directors', methods=['POST'])
@app.route('/pictures', methods=['POST'])
@app.route('/terms', methods=['POST'])
@app.route('/trends_by_decade/2010', methods=['POST'])
@app.route('/trends_by_decade/2000', methods=['POST'])
@app.route('/trends_by_decade/1990', methods=['POST'])
@app.route('/trends_by_decade/1980', methods=['POST'])
@app.route('/trends_by_decade/1970', methods=['POST'])
@app.route('/trends_by_decade/1960', methods=['POST'])
@app.route('/trends_by_decade/1950', methods=['POST'])
@app.route('/trends_by_decade/1940', methods=['POST'])
@app.route('/trends_by_decade/1930', methods=['POST'])
@app.route('/trends_by_decade/1920', methods=['POST'])
@app.route('/trends_by_decade/1910', methods=['POST'])
@app.route('/trends', methods=['POST'])
@app.route('/winners2020', methods=['POST'])
def my_form_post():
    ds = backend.datasource.DataSource()

    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)
    winners = []
    key = request.form['key']
    length = len(key)

    # when the input was year
    if length == 4:
        year = int(key)
        categories = ["picture","actor","actress","director"]

        if year < 1927 or year > 2018:
            title =  'The year ' + str(year) + ' is out of range. Please go back and type in again.'
            return render_template('result1.html', winners=[], year=year, title=title)
        else:
            winners.append({"award":"Award", "film":"Film", "person":"Person"})
            for category in categories:
                result = ds.get_winner(connection, year, category)
                film = result[0][0]
                if category != "picture":
                    person = result[0][1]
                else:
                    person = ""
                winners.append({"award":category, "film":film, "person":person})
                title = str(year) + ' Oscar Winners'
        return render_template('result1.html', winners=winners, title=title)
    else:
        year = int(key[:4])
        length = len(key)
        category = str(key[10:length])
        title = str(key[5:]) + " of " + str(year)
        picture = ds.get_by_year(connection, year, category)
        person = ds.get_winner(connection, year, category)[0]
        return render_template('result2.html', title= title, person=person, year=year, category=category, picture=picture[0])

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


@app.route('/pictures/<filter_type>')
def pictures_by_genre(filter_type):
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    year = 0
    category = "picture"
    pictures = ds.get_winner(connection, year, category)
    
    results = []

    genres_with_pictures = []
    for picture in pictures:
        if filter_type == 'genre':
            
            genre = ds.get_by_picture(connection, 'genre', picture)
            genres_with_pictures.append({"genre": genre, "picture":picture})

    results =  [{'genre': 'Drama', 'pictures': []},
                {'genre': 'Sport', 'pictures': []},
                {'genre': 'History', 'pictures': []},
                {'genre': 'Comedy', 'pictures': []},
                {'genre': 'Biography', 'pictures': []},
                {'genre': 'Crime', 'pictures': []},
                {'genre': 'Adventure', 'pictures': []},
                {'genre': 'Action', 'pictures': []},
                {'genre': 'Western', 'pictures': []},
                {'genre': 'Musical', 'pictures': []},
                {'genre': 'Romance', 'pictures': []},
                {'genre': 'Thriller', 'pictures': []},
                {'genre': 'Mystery', 'pictures': []},
                {'genre': 'Sci-Fi', 'pictures': []},
                {'genre': 'Family', 'pictures': []}]


    for genre_with_pictures in genres_with_pictures:
        for result in results:
            genre = genre_with_pictures["genre"]
            picture = genre_with_pictures["picture"]
            year = ds.get_by_picture(connection, 'yearOfRelease', picture)
            picture_name = picture + '(' + year + ')'
            if result["genre"] == genre_with_pictures:
                results["picture"].append(picture_name)

    return render_template('filtered-pictures.html', results=results)


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


@app.route('/trends_by_decade/<decade>')
def trends_by_decade(decade):
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    if int(decade) == 2010:
        start = 2010
        end = 2018
    elif int(decade) == 1910:
        start = 1927
        end = 1929
    else:
        start = int(decade)
        end = int(decade)+9
    pictures = ds.get_pictures(connection, start, end)
    genres = ds.get_genre(connection, pictures)
    counts = ds.count_genre(connection, genres)

    return render_template('trends-by-decade.html', start=start, end=end, counts=counts)


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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')





if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
