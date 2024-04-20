from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student.id'))  # Optional, if using Student model
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    mark = db.Column(db.Float)
    feedback = db.Column(db.Text)
    criteria = db.Column(db.Text)
    date = db.Column(db.DateTime)
    # ... Consider additional attributes like grading criteria and date
