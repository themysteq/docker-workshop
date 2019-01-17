from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World! I am flask! from compose :) '

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0')
