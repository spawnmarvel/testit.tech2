import random as ran
from math import cos
import pygal
from pygal.style import DarkColorizedStyle

def make_graph(graph_style):
    msg = ""
    graph_data = ""
    rv = ran.randint(3, 60)
    try:
        if graph_style == "Line":
            graph = pygal.Line(fill=True, interpolate='cubic', style=DarkColorizedStyle)
            graph.title = "Timeline year soda sales in mil"
            graph.x_labels = ["2000", "2001", "2003", "2004", "2005"]
            graph.add("Pepsi", [rv, rv+20, rv-5, rv+3, rv+12])
            graph.add("Coca Cola", [rv+5, rv+18, rv-5, rv+20, rv+25])
            graph.add("Sprite", [rv, rv+6, rv-9, rv+5, rv+12])
            graph.add("Orange", [rv+4, rv+30, rv-10, rv, rv+8])
            graph_data = graph.render_data_uri()
            msg = "Line"
        elif graph_style == "Bar":
            graph = pygal.Bar(fill=True, interpolate='cubic', style=DarkColorizedStyle)
            graph.title = "Timeline year soda sales in mil"
            graph.x_labels = ["2000", "2001", "2003", "2004", "2005"]
            graph.add("Pepsi", [rv, rv+20, rv-5, rv+3, rv+12])
            graph.add("Coca Cola", [rv+5, rv+18, rv-5, rv+20, rv+25])
            graph.add("Sprite", [rv, rv+6, rv-9, rv+5, rv+12])
            graph.add("Orange", [rv+4, rv+30, rv-10, rv, rv+8])
            graph_data = graph.render_data_uri()
            msg = "Bar"
        elif graph_style == "Treemap":
            treemap = pygal.Treemap(fill=True, interpolate='cubic', style=DarkColorizedStyle)
            treemap.title = 'Binary TreeMap'
            treemap.add('A', [2, 1, 12, 4, 2, 1, 1, 3, 12, 3, 4, None, 9])
            treemap.add('B', [4, 2, 5, 10, 3, 4, 2, 7, 4, -10, None, 8, 3, 1])
            treemap.add('C', [3, 8, 3, 3, 5, 3, 3, 5, 4, 12])
            treemap.add('D', [23, 18])
            treemap.add('E', [1, 2, 1, 2, 3, 3, 1, 2, 3, 4, 3, 1, 2, 1, 1, 1, 1, 1])
            treemap.add('F', [31])
            treemap.add('G', [5, 9.3, 8.1, 12, 4, 3, 2])
            treemap.add('H', [12, 3, 3])
            graph_data = treemap.render_data_uri()
            msg = " Treemap"
        elif graph_style == "Gauge":
            gauge_chart = pygal.Gauge(human_readable=True, fill=True, interpolate='cubic', style=DarkColorizedStyle)
            gauge_chart.title = 'DeltaBlue V8 benchmark results'
            gauge_chart.range = [0, 10000]
            gauge_chart.add('Chrome', 8212)
            gauge_chart.add('Firefox', 8099)
            gauge_chart.add('Opera', 2933)
            gauge_chart.add('IE', 41)
            graph_data = gauge_chart.render_data_uri()
            msg = "Gauge"
        elif graph_style == "SolidGauge":
            gauge = pygal.SolidGauge(inner_radius=0.70, fill=True, interpolate='cubic', style=DarkColorizedStyle)
            percent_formatter = lambda x: '{:.10g}%'.format(x)
            dollar_formatter = lambda x: '{:.10g}$'.format(x)
            gauge.value_formatter = percent_formatter

            gauge.add('Series 1', [{'value': 225000, 'max_value': 1275000}], formatter=dollar_formatter)
            gauge.add('Series 2', [{'value': 110, 'max_value': 100}])
            gauge.add('Series 3', [{'value': 50}])
            gauge.add('Series 4', [{'value': 51, 'max_value': 100},{'value': 12, 'max_value': 100}])
            gauge.add('Series 5', [{'value': 79, 'max_value': 100}])
            gauge.add('Series 6', 99)
            gauge.add('Series 7', [{'value': 100, 'max_value': 100}])
            graph_data = gauge.render_data_uri()
            msg = "SolidGauge"
        elif graph_style == "XY":
            xy_chart = pygal.XY(fill=True, interpolate='cubic', style=DarkColorizedStyle)
            xy_chart.title = 'XY Cosinus'
            xy_chart.add('x = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
            xy_chart.add('y = cos(x)', [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)])
            xy_chart.add('x = 1',  [(1, -5), (1, 5)])
            xy_chart.add('x = -1', [(-1, -5), (-1, 5)])
            xy_chart.add('y = 1',  [(-5, 1), (5, 1)])
            xy_chart.add('y = -1', [(-5, -1), (5, -1)])
            graph_data = xy_chart.render_data_uri()
            msg = "XY"
        elif graph_style == "Multi-series pie":
            pie_chart = pygal.Pie(fill=True, interpolate='cubic', style=DarkColorizedStyle)
            pie_chart.title = 'Browser usage by version in February 2012 (in %)'
            pie_chart.add('IE', [5.7, 10.2, 2.6, 1])
            pie_chart.add('Firefox', [.6, 16.8, 7.4, 2.2, 1.2, 1, 1, 1.1, 4.3, 1])
            pie_chart.add('Chrome', [.3, .9, 17.1, 15.3, .6, .5, 1.6])
            pie_chart.add('Safari', [4.4, .1])
            pie_chart.add('Opera', [.1, 1.6, .1, .5])
            graph_data = pie_chart.render_data_uri()
            msg = "Multi-series pie"

        


    except Exception as e:
        msg = e
    t = (msg, graph_data)
    return t