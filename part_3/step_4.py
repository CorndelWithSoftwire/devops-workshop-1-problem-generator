from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/films/list')
def get_films():
    return app.send_static_file("filmlist.html")


@app.route('/films/table')
def get_template():
    films = []
    stars_filter = request.args and request.args['stars']

    with open("film_reviews.txt", 'r') as file:
        split_lines = [line.split(', ') for line in file.read().splitlines()]
        films = [{'film_name': film_name, 'stars': stars}
                 for [film_name, stars] in split_lines
                 if not stars_filter or stars == stars_filter]

    return render_template("filmtable.jinja", films=films)


if __name__ == '__main__':
    app.run()
