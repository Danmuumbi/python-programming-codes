from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
import os

# Enable SQLAlchemy logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    city = db.Column(db.String(500), nullable=False)
    reporting_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mentors = db.relationship('Mentor', backref='student')  # One mentor can be assigned to a student

class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    teaches = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)  # Relationship with student

if __name__ == "__main__":
    print("Creating tables if they don't exist...")
    db.create_all()
    print("Tables created")
    print("Database path:", os.path.abspath("db.sqlite3"))
    app.run(debug=True)
