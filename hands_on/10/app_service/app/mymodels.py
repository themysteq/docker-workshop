from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json

db = SQLAlchemy()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.name} {self.surname}>"