import marshmallow_sqlalchemy

from books_api.models import Book


class BookSchema(marshmallow_sqlalchemy.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

