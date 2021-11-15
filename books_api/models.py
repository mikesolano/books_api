from app import db


class Book(db.Model):
    """ Book entity to represent rows on the books table """
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
        return f"Book(id={self.id if self.id else None}, " \
               f"title={self.title}, " \
               f"author_first_name={self.author_first_name}, " \
               f"author_last_name={self.author_last_name}, " \
               f"year={self.year})"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, data):
        for key in data:
            setattr(self, key, data[key])
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
