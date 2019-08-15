import os
class Config:
    SECRET_KEY = 'top-secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/sin'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/sin'
class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/sin'

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/sin'
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}