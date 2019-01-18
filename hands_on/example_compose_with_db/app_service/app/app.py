from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.name} {self.surname}>"

@app.route('/')
def hello():
    return 'Hello, World! I am flask! from compose :) '

@app.route('/employees')
def employees():
    result = Employee.query.all()
    dict_res = [{ "name": x.name,"surname": x.surname } for x in result ]
    response = json.dumps(dict_res)
    return response

#@app.route('/employees/{e_id}')
#def employee_details(e_id):
    

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0')
