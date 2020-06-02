from flask import Flask

app = Flask(__name__)


@app.route('/films/list')
def get_films():
    return app.send_static_file("filmlist.html")


if __name__ == '__main__':
    app.run()
