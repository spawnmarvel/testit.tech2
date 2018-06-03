from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from app import db, login_manager

sql_create_users = "create table if not exists user(id INTEGER PRIMARY KEY autoincrement, email char(60) NOT NULL, username char(60) NOT NULL,  password_hash char(60) NOT NULL)"

class User(UserMixin, db.Model):

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    
    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        Werkzeug's handy security helper methods, generate_password_hash, which allows us to hash passwords
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def init_user():
    msg = None
    global conn
    try:
       
        conn = sqlite3.connect("web2.db")
        with conn:
            cur = conn.cursor()
            global sql_create_users
            cur.execute(sql_create_users)
            conn.commit()
            row = cur.fetchone()
            if row == None:
                msg = "Table exists user"
            else:
                msg = "Table created user"
    except sqlite3.OperationalError as e:
        msg = str(e)
    return msg
    

if __name__ == "__main__":
    init_user()

