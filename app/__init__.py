"""___"""
# app/ __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
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
    app.config.from_pyfile("config.conf") # instance config

    Bootstrap(app)
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "Not authorized"
    login_manager.login_view = "auth.login"

    
    # migrate = Migrate(app, db)
    with app.app_context():
        from app import models as d 
        # print(d.init_user())
        # db.create_all()
        from app.note_db import db_note_handler as dbh
        # print(dbh.init_holder())
        # print(dbh.db_insert_note())
        # print(format(dbh.db_all_note()))
        # make admin
        # print(d.make_admin("espen"))
        # print(d.get_user())
    from app.logs import db_logger as db_log
    # print(db_log.init_logger())

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .note import note as note_blueprint
    app.register_blueprint(note_blueprint)

    from .tech import tech as tech_blueprint
    app.register_blueprint(tech_blueprint)

    from .python_tutorials import python_tutorials as python_tutorials_blueprint
    app.register_blueprint(python_tutorials_blueprint)



    return app

    




