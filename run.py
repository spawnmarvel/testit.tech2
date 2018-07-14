# run.py

import os
from flask import render_template

from app import create_app

dv = "development"
pr = "production"

app = create_app(dv)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("/error/400.html")

@app.errorhandler(400)
def handle_bad_request(error):
    return render_template("/error/400.html")

if __name__ == '__main__':
    # for linux
    # app.run(host='0.0.0.0')
    app.run(port=5100)
	# debug should come from config
