
import os


class Config():
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/keep_fit'
      SECRET_KEY = 'f869f86f2c98249f18e72b34f94768f1'
class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True
  


config_options = {
    'development':DevConfig

}