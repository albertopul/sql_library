from app import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True, unique=True)
    genre = db.Column(db.Text)
    year = db.Column(db.Integer)
    artists = db.relationship("Artist", backref="book", lazy="dynamic")
    rented = db.relationship("Rented", backref="book", lazy="dynamic")

    def __str__(self): 
        return f"<Book: {self.title}...>"


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index= True)
    lastname = db.Column(db.String(100), index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    
    def __str__(self):
        return f"<Artist: {self.name} {self.lastname} ...>"


class Rented(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Rented: {self.id} ...>"


