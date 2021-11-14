import marshmallow_sqlalchemy

from app.models import Book


class BookSchema(marshmallow_sqlalchemy.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

