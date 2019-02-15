from flask_marshmallow import Marshmallow
from mymodels import Employee

ma = Marshmallow()


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee
