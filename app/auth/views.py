from flask import flash, redirect, render_template, url_for, session
from flask_login import login_required, login_user, logout_user, current_user, user_logged_in
import datetime
# http://flask-login.readthedocs.io/en/latest/
from . import auth
from app.auth.forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

from app.logs import db_logger

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            username=form.username.data,
                            password=form.password.data)

        # add employee to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        
        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            # log employee in
            login_user(user, duration = datetime.timedelta(seconds=60))
            print(user_logged_in)
            # redirect to the dashboard page after login
            db_logger.db_logit("route login", format(user))
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    db_logger.db_logit("route logout", "user exit")
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))