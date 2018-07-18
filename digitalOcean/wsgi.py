from app import create_app
from flask import render_template


dv = "development"
pr = "production"

app = create_app(pr)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("/error/404.html")

@app.errorhandler(400)
def handle_bad_request(error):
    return render_template("/error/400.html")


if __name__ =="__main__":
   print("\n Success, system path jekl")
   app.run(threaded=True)
