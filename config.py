import os
from flask import config



class Config():
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/fitness'
      SECRET_KEY = 'f869f86f2c98249f18e72b34f94768f1'
      ALLOWED_HOST = 'localhost'
      db_name = 'fitness'
      db_user = 'user'
      db_password = '1234'
class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development':DevConfig

}