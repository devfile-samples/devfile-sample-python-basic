from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/healthy')
def health():
    return ""


@app.route('/fail')
def failing():
    abort(404)


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
