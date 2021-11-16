class Config:
    """ base configuration """
    FLASK_ENV = 'DEFAULT'
    JSON_SORT_KEYS = False


class Development(Config):
    """ development configuration """
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:docker@localhost:5432'
    FLASK_ENV = 'DEV'


class Production(Config):
    """ production configuration """
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'PROD'
