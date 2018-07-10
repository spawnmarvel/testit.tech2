from flask import render_template

from . import tech

@tech.route("/techview")
def tech_view():
    return render_template("tech/pdf_files.html")