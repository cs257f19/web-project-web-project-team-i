@app.route('/pictures/<filter_type>')
def trends_by_decade(filter_type):
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
            genre = genre_with_pictures.genre
            picture = genre_with_pictures.picture
            year = ds.get_by_picture(connection, 'yearOfRelease', picture)
            picture_name = picture + '(' + year + ')'
            if result.genre == genre_with_pictures:
                results.pictures.append(picture_name)

    return render_template('filtered-pictures.html', results=results)
