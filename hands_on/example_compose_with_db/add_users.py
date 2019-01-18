from app import db
from app import Employee

emp1 = Employee(name='moje_imie',surname='mojenazwisko')
emp2 = Employee(name='moje_imie2',surname='mojenazwisko2')
db.session.add(emp1)
db.session.add(emp2)
db.session.commit()
