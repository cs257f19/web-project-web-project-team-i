@app.route('/pictures/<filter_type>')
def trends_by_decade(filter_type):
    ds = backend.datasource.DataSource()
    user = 'kuritar'
    password = 'lamp977python'
    connection = ds.connect(user, password)

    year = 0
    category = "picture"
    pictures = ds.get_winner(connection, year, category)

    if filter_type == 'awards':
        

    return render_template('filtered-pictures.html', )
