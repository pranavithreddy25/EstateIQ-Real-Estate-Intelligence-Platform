import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def str_to_bool(val):
    return str(val).lower() in ('true', '1', 'yes')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'estateiq-dev-secret-key-change-in-production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}

    # Brand Configuration — easily changeable
    BRAND_NAME = os.environ.get('BRAND_NAME', 'Estate IQ')
    BRAND_TAGLINE = os.environ.get('BRAND_TAGLINE', '')
    DEFAULT_CITY = os.environ.get('DEFAULT_CITY', 'Hyderabad')
    DEFAULT_STATE = os.environ.get('DEFAULT_STATE', 'Telangana')

    # Advertisement Module Configuration
    ADS_ENABLED = str_to_bool(os.environ.get('ADS_ENABLED', 'false'))
    ADS_PROVIDER = os.environ.get('ADS_PROVIDER', 'google_adsense')
    ADSENSE_CLIENT_ID = os.environ.get('ADSENSE_CLIENT_ID', '')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'estateiq.db')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test_estateiq.db')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://estateiq_user:strongpassword@localhost/estateiq_db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
