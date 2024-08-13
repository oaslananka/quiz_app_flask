from app.db import db
from datetime import datetime

class QuizResult(db.Model):
    __tablename__ = 'quiz_table'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    quiz_date = db.Column(db.DateTime, default=datetime.utcnow)
