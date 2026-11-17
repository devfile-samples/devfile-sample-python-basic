from flask import Flask make_response
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/healthy')
def health():
    return "", 200


@app.route('/liveness')
def liveness():
    return "alive", 200


@app.route('/fail')
def failing():
    abort(404)


@app.route("/retry")
def retry_after():
    response = make_response("Too many requests", 429)
    response.headers["Retry-After"] = "3"
    return response

@app.route("/data")
def get_data():
    body = jsonify({"error": "Too Many Requests", "retry_after": 2})
    return body, 429, {"Retry-After": "2"}

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
