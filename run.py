from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object('config.Development')
db = SQLAlchemy(app)
ma = Marshmallow(app)
from app import routes, models


if __name__ == '__main__':
    app.run()
