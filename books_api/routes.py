from flask import jsonify, request, make_response
from marshmallow import ValidationError
from books_api.models import Book
from books_api.schemas import BookSchema
from app import app

# create schemas objects
book_schema = BookSchema()
books_schema = BookSchema(many=True)


@app.route('/api/environment', methods=['GET'])
def get_env():
    """ Get current environment """
    return make_response(jsonify({"environment": app.config['FLASK_ENV']}), 200)


@app.route('/api/books', methods=['POST'])
def create_book():
    """ Create a new book """
    try:
        data = book_schema.load(request.get_json())
    except ValidationError as e:
        return make_response(jsonify({"messages": e.messages}), 400)

    book = Book(title=data['title'],
                author_first_name=data['author_first_name'],
                author_last_name=data['author_last_name'],
                year=data['year'] if 'year' in data.keys() else None)
    result = book_schema.dump(book.create())

    return make_response(jsonify(book_schema.dump(result)), 201)


@app.route('/api/books', methods=['GET'])
def get_books():
    """ Get all books """
    books = books_schema.dump(Book.query.all())
    return make_response(jsonify({"books": books}), 200)


@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    """ Get a single book """
    book = book_schema.dump(Book.query.get(id))
    if not book:
        return make_response({"message": "Book not found"}, 400)
    else:
        return make_response(jsonify(book), 200)


@app.route('/api/books/<int:id>', methods=['PUT', 'PATCH'])
def update_book(id):
    """ Update a book """
    book = Book.query.get(id)
    if not book:
        return make_response({"message": "Book not found"}, 400)
    else:
        try:
            if request.method == 'PUT':
                data = book_schema.load(request.get_json())
            else:
                data = book_schema.load(request.get_json(), partial=True)
        except ValidationError as e:
            return make_response(jsonify({"messages": e.messages}), 400)
        result = book_schema.dump(book.update(data))
        return make_response(jsonify(result), 200)


@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """ Delete a book """
    book = Book.query.get(id)
    if not book:
        return make_response({"message": "Book not found"}, 400)
    result = book_schema.dump(book.delete())
    return make_response(jsonify(result), 200)



