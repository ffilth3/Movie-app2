from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MovieModel(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    format = db.Column(db.String, nullable=False)
    actors = db.Column(db.String, nullable=False)
