# https://pythonprogramming.net/pygal-tutorial/
# pygal

from flask import render_template, request
import pygal
import random as ran

from . import python_tutorials
from . import graph_util as Graph_util

@python_tutorials.route("/pypygal", methods=['GET', 'POST'])
def py_pygal():
    msg = None
    rv = ran.randint(10, 300)
    msg = ""
    graph_data = ""
    if request.method == "POST":
        if request.form["action"] == "View":
            graph_style = request.form["selectvalueadd"]
            tmp = Graph_util.make_graph(graph_style)
            msg = tmp[0]
            graph_data = tmp[1]
            return render_template("python_tutorials/python_pygal.html", graph_data=graph_data, msg=msg)
    # GET
    tmp = Graph_util.make_graph("SolidGauge")
    msg = tmp[0]
    graph_data = tmp[1]
    return render_template("python_tutorials/python_pygal.html", graph_data=graph_data, msg=msg)


@python_tutorials.route("/forensic", methods=['GET', 'POST'])
def py_forensic():
    return render_template("python_tutorials/python_forensic.html")


