from app import app, db, routes, models
from app.models import Book, Artist, Rented

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book": Book,
        "Artist": Artist,
        "Rented": Rented,
    }




