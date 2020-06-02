from flask import Flask, render_template

app = Flask(__name__)


@app.route('/films/list')
def get_films():
    return app.send_static_file("filmlist.html")


@app.route('/films/table')
def get_template():
    films = []

    with open("film_reviews.txt", 'r') as file:
        split_lines = [line.split(', ') for line in file.read().splitlines()]
        films = [{'film_name': film_name, 'stars': stars}
                 for [film_name, stars] in split_lines]

    return render_template("filmtable.jinja", films=films)


if __name__ == '__main__':
    app.run()
