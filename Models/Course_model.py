from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    Lecturer_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'))  # Optional, if using User model

    # ... Define relationships with other models (e.g., exams)
    Lecturer = db.relationship(
        'User', backref='courses', foreign_keys=[Lecturer_id])
