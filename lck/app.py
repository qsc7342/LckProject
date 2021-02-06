from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_cors import CORS
import time
import requests
from bs4 import BeautifulSoup

DEBUG = True
app = Flask(__name__)
# enable CORS
app.config.from_object(__name__)
app.secret_key = 'some_secret'
CORS(app)


### Routes for customer part start ###
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rank')
def rank():

    return render_template('rank.html')


if __name__ == '__main__':
    app.run()
