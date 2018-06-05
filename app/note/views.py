from flask import render_template
from flask_login import login_required

from . import note

@note.route("/note")
@login_required
def note():
    """
    Render the note template on the / route
    """
    return render_template("note/note.html")