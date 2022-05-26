from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT'))

    if port == None:
        port = 8080

    app.run(port=port,host='0.0.0.0')