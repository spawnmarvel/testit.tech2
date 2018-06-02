# run.py

import os

from app import create_app

dv = "development"
pr = "production"

app = create_app(dv)

if __name__ == '__main__':
    app.run(port=5100)
	# debug should come from config
