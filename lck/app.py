<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_cors import CORS
import time
import requests
from bs4 import BeautifulSoup
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# db = SQLAlchemy()
# migrate = Migrate()
DEBUG = True


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.secret_key = 'some_secret'
    CORS(app)
    from views import mainpage, teamrankpage
    app.register_blueprint(mainpage.bp)
    app.register_blueprint(teamrankpage.bp)
    return app


if __name__ == '__main__':
    app.run()
=======
from flask import Flask, render_template, request, redirect ,url_for, flash, session
from flask_cors import CORS
import time
import requests
from bs4 import BeautifulSoup
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()
DEBUG = True
def create_app():
	app = Flask(__name__)
	app.config.from_object(config)
	db.init_app(app)
	migrate.init_app(app, db)
	import schema
	app.secret_key = 'some_secret'
	CORS(app)
	from views import mainpage, teamrankpage, insertpage
	app.register_blueprint(mainpage.bp)
	app.register_blueprint(teamrankpage.bp)
	app.register_blueprint(insertpage.bp)
	return app

if __name__ == '__main__':
	app.run()
>>>>>>> a1af914cce11f4333a714e107e727d6941043a9b
