
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(80), unique=True, nullable=False)
    Last_name = db.Column(db.String(80), unique=True, nullable=False)
    registration_number = db.Column(db.String(80), unique=True, nullable=False)
    # ... Define student-specific attributes (e.g., name, registration number)

    # ... Define relationships with other models (e.g., courses enrolled)
