from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/healthy')
def health():
    return 200


@app.route('/liveness')
def liveness():
    return 200


@app.route('/fail')
def failing():
    abort(404)

@app.route("/data")
def get_data():
    body = jsonify({"error": "Too Many Requests", "retry_after": 2})
    return body, 429, {"Retry-After": "2"}

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
