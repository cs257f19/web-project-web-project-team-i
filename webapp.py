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
@app.route('/pictures', methods=['POST'])
@app.route('/pictures/Drama', methods=['POST'])
@app.route('/pictures/Comedy', methods=['POST'])
@app.route('/pictures/Action', methods=['POST'])
@app.route('/pictures/Romance', methods=['POST'])
@app.route('/pictures/Thriller', methods=['POST'])
@app.route('/pictures/Biography', methods=['POST'])
@app.route('/pictures/Adventure', methods=['POST'])
@app.route('/pictures/Musical', methods=['POST'])
@app.route('/pictures/Family', methods=['POST'])
@app.route('/pictures/History', methods=['POST'])
@app.route('/actors', methods=['POST'])
@app.route('/actors/Drama', methods=['POST'])
@app.route('/actors/Comedy', methods=['POST'])
@app.route('/actors/Action', methods=['POST'])
@app.route('/actors/Romance', methods=['POST'])
@app.route('/actors/Thriller', methods=['POST'])
@app.route('/actors/Biography', methods=['POST'])
@app.route('/actors/Adventure', methods=['POST'])
@app.route('/actors/Musical', methods=['POST'])
@app.route('/actors/Family', methods=['POST'])
@app.route('/actors/History', methods=['POST'])
@app.route('/actresses', methods=['POST'])
@app.route('/actresses/Drama', methods=['POST'])
@app.route('/actresses/Comedy', methods=['POST'])
@app.route('/actresses/Action', methods=['POST'])
@app.route('/actresses/Romance', methods=['POST'])
@app.route('/actresses/Thriller', methods=['POST'])
@app.route('/actresses/Biography', methods=['POST'])
@app.route('/actresses/Adventure', methods=['POST'])
@app.route('/actresses/Musical', methods=['POST'])
@app.route('/actresses/Family', methods=['POST'])
@app.route('/actresses/History', methods=['POST'])
@app.route('/directors', methods=['POST'])
@app.route('/directors/Drama', methods=['POST'])
@app.route('/directors/Comedy', methods=['POST'])
@app.route('/directors/Action', methods=['POST'])
@app.route('/directors/Romance', methods=['POST'])
@app.route('/directors/Thriller', methods=['POST'])
@app.route('/directors/Biography', methods=['POST'])
@app.route('/directors/Adventure', methods=['POST'])
@app.route('/directors/Musical', methods=['POST'])
@app.route('/directors/Family', methods=['POST'])
@app.route('/directors/History', methods=['POST'])
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
@app.route('/trends', methods=['POST'])
@app.route('/winners2020', methods=['POST'])
@app.route('/terms_of_use', methods=['POST'])
@app.route('/contact_us', methods=['POST'])

def my_form_post():
    ds = backend.datasource.DataSource()

    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)
    winners = []
    key = request.form['key']
    length = len(key)

    #When user searches by Year
    if length == 4:
        year = str(key)
        integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for ch in year:
            if ch not in integers:
                title =  'The year ' + str(year) + ' is invalid. Please type in four integers.'
                return render_template('result1.html', winners=[], year=year, title=title)
        year = int(year)
        categories = ["picture","actor","actress","director"]
        #if year out of range, return error message
        if year < 1928 or year > 2018:
            title =  'The year ' + str(year) + ' is out of range. Please go back and type in again.'
            return render_template('result1.html', winners=[], year=year, title=title)
        #if year is in the valid range, return all winners from that year
        else:
            for category in categories:
                result = ds.get_winner(connection, year, category)
                film = result[0][0]
                if category != "picture":
                    person = result[0][1]
                else:
                    person = ""
                category = "Best " + category.title()
                winners.append({"award":category, "film":film, "person":person})
                title = str(year) + ' Oscar Winners'
        return render_template('result1.html', winners=winners, title=title)
    #When user searches Year + Category
    else:
        #Check whether year is valid
        year = str(key[:4])
        integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for ch in year:
            if ch not in integers:
                title =  'The year ' + str(year) + ' is invalid. Please type in four integers.'
                return render_template('result1.html', winners=[], year=year, title=title)
        year = int(year)

        #Check whether category is valid
        length = len(key)
        category = str(key[10:length])
        if year < 1927 or year > 2018:
            title =  'The year ' + str(year) + ' is out of range. Please go back and type in again.'
            person = None
            picture = [None, None, None, None, None, None]
            display = False
        elif category != 'picture' and category != 'actor' and category != 'actress' and category != 'director':
            input_cat = str(key[5:length])
            person = None
            picture = [None, None, None, None, None, None]
            title = input_cat.title() + ' is not a valid category. Please type either "best picture", "best actor", "best actoress", "best director".'
            display = False
        else:
            title_cat = str(key[5:])
            title = title_cat.title() + " of " + str(year)
            picture = ds.get_by_year(connection, year, category)
            person = ds.get_winner(connection, year, category)[0]
            display = True
        return render_template('result2.html', title= title, person=person, year=year, category=category, picture=picture[0], display=display)


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

@app.route('/pictures/<genre>')
def pictures_by_genre(genre):
    '''
    Retrieve genre-specific Best Picture winners

    PARAM: String genre
    RETURN: html page containing Best Picture winning genres and counts
    '''
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    year = 0
    category = "picture"
    pictures = ds.get_winner(connection, year, category)

    '''
    Iterating through all movies that won best picture
    Filtering them by the given genre
    '''
    results = []
    genres_with_pictures = []
    for picture in pictures:
        name = picture[0]
        if type(name) == str:
            if "'" not in name:
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[1]})
            else:
                name = name.replace("'", "''")
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[1]})

    return render_template('filtered-pictures.html', genre=genre, results=results)

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

@app.route('/actors/<genre>')
def actors_by_genre(genre):
    '''
    Retrieve genre-specific Best Actor winners

    PARAM: String genre
    RETURN: html page containing Best Actor winning genres and counts
    '''
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    year = 0
    category = "actor"
    pictures = ds.get_winner(connection, year, category)

    '''
    Iterating through all movies that won best actor
    Filtering them by the given genre
    '''
    results = []
    genres_with_pictures = []
    for picture in pictures:
        name = picture[0]
        if type(name) == str:
            if "'" not in name:
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[2], "person":picture[1]})
            else:
                name = name.replace("'", "''")
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[2], "person":picture[1]})

    return render_template('filtered-actors.html', genre=genre, results=results)

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

@app.route('/actresses/<genre>')
def actresses_by_genre(genre):
    '''
    Retrieve genre-specific Best Actress winners

    PARAM: String genre
    RETURN: html page containing Best Actress winning genres and counts
    '''
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    year = 0
    category = "actress"
    pictures = ds.get_winner(connection, year, category)

    '''
    Iterating through all movies that won best actress
    Filtering them by the given genre
    '''
    results = []
    genres_with_pictures = []
    for picture in pictures:
        name = picture[0]
        if type(name) == str:
            if "'" not in name:
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[2], "person":picture[1]})
            else:
                name = name.replace("'", "''")
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[2], "person":picture[1]})

    return render_template('filtered-actresses.html', genre=genre, results=results)


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

@app.route('/directors/<genre>')
def directors_by_genre(genre):
    '''
    Retrieve genre-specific Best Director winners

    PARAM: String genre
    RETURN: html page containing Best Director winning genres and counts
    '''
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    year = 0
    category = "director"
    pictures = ds.get_winner(connection, year, category)

    '''
    Iterating through all movies that won best director
    Filtering them by the given genre
    '''
    results = []
    genres_with_pictures = []
    for picture in pictures:
        name = picture[0]
        if type(name) == str:
            if "'" not in name:
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[2], "person":picture[1]})
            else:
                name = name.replace("'", "''")
                quered_genre = ds.get_by_picture(connection, 'genre', name)
                if quered_genre == genre:
                    results.append({"picture": name, "year":picture[2], "person":picture[1]})

    return render_template('filtered-directors.html', genre=genre, results=results)

@app.route('/trends_by_decade/<decade>')
def trends_by_decade(decade):
    '''
    Retrieve information about Oscar winners by decade

    PARAM: Integer decade
    RETURN: html page containing all stats about Oscar winners from given decade
    '''
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    if int(decade) == 2010:
        start = 2010
        end = 2018
    elif int(decade) == 1920:
        start = 1928
        end = 1930
    else:
        start = int(decade)
        end = int(decade)+9
    pictures = ds.get_pictures(connection, start, end)
    genres = ds.get_genre(connection, pictures)
    counts = ds.count_genre(connection, genres)

    scores = ds.get_Score(connection, start, end)
    avgScores = ds.get_avgScore(connection, scores)

    ratings = ds.get_Rating(connection, start, end)
    avgRatings = ds.get_avgRating(connection, ratings)

    categories = ["picture","actor","actress","director"]
    infos = []

    '''
    Adding award category, film and celebrity to winners array
    by iterating thru all films that won specified category 
    in the specified decade.
    '''
    for year in range(start, end+1):
        winners = []
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
        infos.append([year, winners])

    return render_template('trends-by-decade.html', start=start, end=end, counts=counts, avgScores=avgScores, avgRatings=avgRatings, infos=infos)

#Routes for all remaining links in header and footer
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
