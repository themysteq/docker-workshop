from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from mymodels import Employee
from myschema import EmployeeSchema
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def hello():
    return 'Hello, World! I am flask! from compose :) '

@app.route('/employees')
def employees():
    result = Employee.query.all()
    e_schema = EmployeeSchema()
    e_data = e_schema.dump(result).data
    #dict_res = [{ "name": x.name, "surname": x.surname } for x in result ]
    #response = json.dumps(dict_res)

    return json.dumps(e_data)

#@app.route('/employees/{e_id}')
#def employee_details(e_id):
    

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0')
