from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

def create_table_if_not_exists():
    with app.app_context():
        db.create_all()
