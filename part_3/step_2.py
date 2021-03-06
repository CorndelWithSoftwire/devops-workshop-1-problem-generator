from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/films/list')
def get_films():
    return send_from_directory("static", "filmlist.html")


if __name__ == '__main__':
    app.run()
