from flask import Flask
import os
import signal
#FLASK_PORT = os.environ.get('FLASK_PORT' ,5000)
app = Flask(__name__)

def sigterm_handler(signum, frame):
    print('Signal handler called with signal', signum)
    exit(128+signum)

@app.route('/')
def hello():
    return 'Hello, World! I am flask!'

if __name__ == '__main__':
#    app.run()
    signal.signal(signal.SIGTERM, sigterm_handler)
    app.run(host='0.0.0.0')
