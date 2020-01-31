from app import db
from sqlalchemy.dialects.postgresql import ARRAY


class teleusers(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Firsttime = db.Column(db.Integer)


class data(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Futures = db.Column(db.Text)
    Data = db.Column(db.Text)