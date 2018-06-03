"""___"""
# app/ __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# Migrations allow us to manage changes we make to the models, and propagate these changes in the databas
from flask_migrate import Migrate

from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

# We've created a function, create_app that, given a configuration name, loads the correct configuration from the config.py file,
# as well as the configurations from the instance/config.py file. 
# We have also created a db object which we will use to interact with the database.
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name]) #object config
    
    app.config.from_pyfile("config.py") # instance config
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "Not authorized"
    login_manager.login_view = "home.index"

    # migrate = Migrate(app, db)
    with app.app_context():
        from app import models
        db.create_all()

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    

    return app




