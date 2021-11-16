from app import ma
from books_api.models import Book


class BookSchema(ma.SQLAlchemyAutoSchema):
    """ Schema for the Book entity """
    class Meta:
        model = Book
        ordered = True

    _links = ma.Hyperlinks(
        {
            'self': ma.URLFor('get_book', id='<id>'),
            'collection': ma.URLFor('get_books')
        }
    )

