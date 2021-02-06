from flask import Flask, render_template, request, redirect ,url_for, flash, session
from flask_cors import CORS
import pymysql
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
def test():
	url = "http://ncov.mohw.go.kr/"

	response = requests.get(url)
	dom_a = BeautifulSoup(response.content, 'html.parser')

	update_time = dom_a.select_one('body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > h2 > a > span.livedate').text.strip()


	return render_template('test.html',data = update_time)


if __name__ == '__main__':
	app.run()
