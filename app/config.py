import os


class Config:
    SECRET_KEY = '@Key1621'
    SQLALCHEMY_DATABASE_URI = 'postgresql://moringa:1234@localhost/fitness'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):

    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
