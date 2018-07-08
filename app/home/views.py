"""___"""
import logging
from flask import render_template, abort, redirect, url_for
from flask_login import login_required, current_user


from . import home
from app.logs import db_logger
from app.db_note import db_handler

@home.route("/")
def index():
    """
    Render the homepage template on the / route
    """
    return render_template("home/index.html")

@home.route("/view")
def index_view():
    """
    Render the homepage template on the / route
    """
    return render_template("home/index_view.html")

@home.route("/about")
def about():
    """
    Render the about template on the / route
    """
    return render_template("home/about.html")

@home.route("/dashboard")
@login_required
def dashboard():
    """
    Render the note template on the / route
    """
    if not current_user.is_admin:
        return redirect(url_for('home.index_view'))
    db_logger.db_logit("route dashboard", "user entry")
    return render_template("home/dashboard.html")


@home.route("/loggerDash")
@login_required
def loggerDash():
    """
    Render the note template on the / route
    """
    if not current_user.is_admin:
        abort(403)
    rv = db_logger.db_logger_all()
    db_logger.db_logit("route loggerDash", "user entry")
    return render_template("home/logger.html", rv=rv)





