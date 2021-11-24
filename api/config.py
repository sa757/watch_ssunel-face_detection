import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'NEED TO BE UPDATED'
    SERVER_PORT = None
    # UPLOAD_FOLDER = UPLOAD_FOLDER


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'hae_optlab_202008'
    SERVER_PORT: os.environ.get('APP_PORT')
