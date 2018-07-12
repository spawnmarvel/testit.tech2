# https://pythonprogramming.net/pygal-tutorial/
# pygal

from flask import render_template, request
import pygal
import random as ran

from . import python_tutorials

@python_tutorials.route("/pypygal", methods=['GET', 'POST'])
def py_pygal():
    msg = None
    rv = ran.randint(10, 300)
    if request.method == "POST":
        if request.form["action"] == "RandomNr":
            try:
                graph = pygal.Line()
                graph.title = "Timeline year soda sales in mil"
                graph.x_labels = ["2000", "2001", "2003", "2004", "2005"]
                graph.add("Pepsi", [rv, rv+20, rv-5, rv+3, rv+12])
                graph.add("Coca Cola", [rv+5, rv+18, rv-5, rv+20, rv+25])
                graph.add("Sprite", [rv, rv+6, rv-9, rv+5, rv+12])
                graph.add("Orange", [rv+4, rv+30, rv-10, rv, rv+8])

                graph_data = graph.render_data_uri()
                msg = "Loaded graph"
                return render_template("python_tutorials/python_pygal.html", graph_data=graph_data, msg=msg)
            except Exception as e:
                msg = e
    #GET
    graph = pygal.Line()
    graph.title = "Timeline year soda sales in mil"
    graph.x_labels = ["2000", "2001", "2003", "2004", "2005"]
    graph.add("Pepsi", [rv, rv+20, rv-5, rv+30, rv+12])
    graph.add("Coca Cola", [rv+5, rv+18, rv-5, rv+39, rv+25])
    graph.add("Sprite", [rv, rv+6, rv-9, rv+9, rv+12])
    graph.add("Orange", [rv+4, rv+30, rv-10, rv, rv+8])

    graph_data = graph.render_data_uri()
    return render_template("python_tutorials/python_pygal.html", graph_data=graph_data, msg=msg)