from flask import Flask
from platform import python_version
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    version = "\nCurrent Version of Python interpreter - "+ python_version()
    date_var = datetime.datetime.now()
    output_str = "Hello World!<br><br>Current Date:"+str(date_var)+"<br><br>"+version
    print("Current Date: "+str(date_var))
    print("Current Version of Python interpreter -", python_version())
    return output_str

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')