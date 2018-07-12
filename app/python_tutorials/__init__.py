from flask import Blueprint

python_tutorials = Blueprint("python_tutorials", __name__)

from . import views