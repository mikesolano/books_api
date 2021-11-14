from flask import jsonify, request

from app.models import Book
from app.schemas import BookSchema
from run import app


@app.route('/api/environment', methods=["GET"])
def get_env():
    return app.config['FLASK_ENV']


@app.route('/api/books', methods=["GET"])
def get_books():
    books_schema = BookSchema(many=True)
    return jsonify(books_schema.dump(Book.query.all()))


@app.route('/api/books', methods=['POST'])
def create_book():
    book_schema = BookSchema()
    data = book_schema.load(request.get_json())
    book = Book(title=data['title'],
                author_first_name=data['author_first_name'],
                author_last_name=data['author_last_name'],
                year=data['year'])
    result = book_schema.dump(book.create())
    return jsonify(book_schema.dump(result))


@app.route('/api/books/<int:id>', methods=["GET"])
def get_book(id):
    book_schema = BookSchema()
    return jsonify(book_schema.dump(Book.query.get(id)))



