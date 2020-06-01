from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route('/films/list')
def get_films():
    return app.send_static_file("filmlist.html")

@app.route('/films/table')
def get_template():
    films =[]

    with open("film_reviews.txt", 'r') as file:
        for line in file.read().splitlines():
            [film_name, stars] = line.split(', ')
            films.append({'film_name': film_name, 'stars': stars})
    
    stars_filter = request.args and request.args['stars']

    if stars_filter:
        films = list(filter(lambda film : film['stars'] == stars_filter, films))

    return render_template("filmtable.jinja", films = films)

if __name__ == '__main__':
    app.run()