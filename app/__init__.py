"""___"""
# app/ __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manger = LoginManager()

# We've created a function, create_app that, given a configuration name, loads the correct configuration from the config.py file,
# as well as the configurations from the instance/config.py file. 
# We have also created a db object which we will use to interact with the database.
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manger.init_app(app)
    login_manger.login_message = "Not authorized"
    login_manger.login_view = "auth.login"


    @app.route("/")
    def test():
        return "hello world"
    

    return app



