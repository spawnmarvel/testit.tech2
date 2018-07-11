# testit.tech 2
# v 1.1
testit.tech, website built for learning Python webdevelopment and
for documenting the stuff I try out. I.e Zabbix, Grafana, Octopus, etc.
It also contains a blog section bulit with SQLite, tab->SQLite->Note Blog.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
<br>
create sqlite db:
(web2) flask db init_
<br>
Example config:
<br>
instance/config.conf
<br>
SECRET_KEY = "gnfwogwvowvgvgwo78794vawvvw"
<br>
SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.db"
<br>
SQLALCHEMY_TRACK_MODIFICATIONS = False
### Prerequisites

TBD

### Code choices
I chose not to have static and templates directories for each blueprint, because all the application templates will inherit from the same base template and use the same CSS file. Instead, the templates directory will have sub-directories for each blueprint so that blueprint templates can be grouped together.
### Installing

Create a virtual env and install all the packets from requirements.txt
## Running the tests
Explain how to run the automated tests for this system
### Break down into end to end tests
Explain what these tests test and why

```
Give an example
```
### And coding style tests
Explain what these tests test and why
```
Give an example
```
## Deployment
Add additional notes about how to deploy this on a live system:
This system is deployed on Digital Ocean running Ubuntu 16.04.3 LTS
The website is served running gunicorn and Nginx

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [SQLite](https://www.sqlite.org/) - Database
* [Bootstrap](https://getbootstrap.com/) - Bootstrap
* [gunicorn](http://gunicorn.org/) - gunicorn
* [nginx](https://www.nginx.com/resources/wiki/) - nginx

## Versioning
Branch: master and test.
For the versions available, see the [tags on this repository](https://github.com/spawnmarvel/testit.tech2). 

## Authors

* **spawnmarvel** - *Initial work* - 


## License


## Acknowledgments

* Tab->Links used (all the most important stuff for building this site)
* Code that was used and inspiration
* + https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one
* + https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two
* + https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three










