from flask import Flask
import os
#FLASK_PORT = os.environ.get('FLASK_PORT' ,5000)
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! I am flask!'

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0')
