# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    #SQLALCHEMY_ECHO: setting this to True helps us with debugging by allowing SQLAlchemy to log errors.
    SQLALCHEMY_ECHO = True
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}