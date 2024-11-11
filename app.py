from flask import Flask
from platform import python_version
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = "\nCurrent Version of Python interpreter - "+ python_version()
    print("Current Version of Python interpreter -", python_version())
    return version

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')