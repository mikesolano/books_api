import marshmallow_sqlalchemy

from books_api.models import Book


class BookSchema(marshmallow_sqlalchemy.SQLAlchemyAutoSchema):
    """ Schema for the Book entity """
    class Meta:
        model = Book

