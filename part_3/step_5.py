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

@app.route('/films/submit', methods=['GET'])
def get_form():
    return render_template("filmsubmit.jinja", message = None)

@app.route('/films/submit', methods=['POST'])
def create_film():
    with open("./film_reviews.txt", 'a') as file:
        file.write(f"{request.form['film-name']}, {request.form['stars']}\n")

    return render_template("filmsubmit.jinja", message={"content": "Successfully Submitted Film!"})

if __name__ == '__main__':
    app.run()