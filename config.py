# config.py

class Config(object):
    """
    Common configurations
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    #SQLALCHEMY_ECHO: setting this to True helps us with debugging by allowing SQLAlchemy to log errors.
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}