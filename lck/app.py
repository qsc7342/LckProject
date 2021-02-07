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
def MainPage():
    return render_template('index.html')


@app.route('/rank')
def Rank():

    # 팀 순위 크롤링
    b = 1
    url = "https://namu.wiki/w/2021%20LoL%20Champions%20Korea%20Spring"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    rank = soup.select(
        '#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(15) > div > table > tbody')
    t = []
    k = []
    r = []
    for x in rank:
        tr_tag = x.find_all('tr')
        for y in tr_tag:
            td_tag = y.find_all('td')
            for q in td_tag:
                div_tag = q.find_all('div')
                for s in div_tag:
                    digit = s.get_text()
                    t.append(digit)
    six = 0
    four = 3

    for i in range(11, 98):
        if(six == 6):
            four -= 1
            if(four > 0):
                continue
            else:
                r.append(k)
                k = []
                four = 3
                six = 0
        else:
            six += 1
            k.append(t[i])
            if(i == 97):
                r.append(k)

    for team in range(0, 10):
        r[team].append("../static/image/team/" + r[team][0] + ".png")

    # 선수 POG순위 크롤링
    response = requests.get(url)
    ranking = soup.select_one(
        "#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(31) > div")
    pog_ranks = ranking.find_all('td')
    pog_data = []
    for pog_rank in pog_ranks:
        pog_data.append(pog_rank.get_text())
        print(pog_rank.get_text())
    return render_template('rank.html', data_list=r)


if __name__ == '__main__':
    app.run()
