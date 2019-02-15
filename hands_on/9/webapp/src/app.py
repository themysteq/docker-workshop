from flask import Flask
import os
import redis
import json
FLASK_PORT = os.environ.get('FLASK_PORT')
app = Flask(__name__)
r = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'),
                port=os.environ.get('REDIS_PORT', 6379), db=0)


@app.route('/')
def hello():
    value = r.incr('count')
    print(value)
    return json.dumps({'visits: ' :str(value)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(FLASK_PORT))
