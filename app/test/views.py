from flask import session, render_template
from . import test

@test.route("/test")
def test_view():
    rv = ""
    if "visits" in session:
        session["visits"] = session.get("visits") + 1
    else:
        session["visits"] = 1 # first entry
    rv = "visits " + format(session.get("visits"))
    return render_template("test/test.html", rv=rv)

@test.route("/del")
def test_del():
    rv = ""
    rv = format(session.pop("visits", None)) # delet
    return render_template("test/test.html", rv=rv)

    