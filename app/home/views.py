"""___"""
import logging
from flask import render_template
from flask_login import login_required


logger = logging.getLogger(__name__)

from . import home

@home.route("/")
def index():
    """
    Render the homepage template on the / route
    """
    logger.debug("index route")
    return render_template("home/index.html")

@home.route("/about")
def about():
    """
    Render the about template on the / route
    """
    logger.debug("about route")
    return render_template("home/about.html")

@home.route("/note")
@login_required

def note():
    """
    Render the note template on the / route
    """




