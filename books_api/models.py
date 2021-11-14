from app import db


class Book(db.Model):
    __tablename__ = 'books'

    # column to property mapping
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(),
        nullable=False
    )
    author_first_name = db.Column(
        db.String(),
        nullable=False
    )
    author_last_name = db.Column(
        db.String(),
        nullable=False
    )
    year = db.Column(
        db.Integer,
        nullable=True
    )

    def __init__(self, title, author_first_name, author_last_name, year):
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.year = year

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Book {self.title}"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
