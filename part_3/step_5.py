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


@app.route('/films/submit', methods=['GET'])
def get_form():
    return render_template("filmsubmit.jinja", message=None)


@app.route('/films/submit', methods=['POST'])
def create_film():
    with open("./film_reviews.txt", 'a') as file:
        file.write(f"{request.form['film-name']}, {request.form['stars']}\n")

    return render_template("filmsubmit.jinja", message={"content": "Successfully Submitted Film!"})


if __name__ == '__main__':
    app.run()
