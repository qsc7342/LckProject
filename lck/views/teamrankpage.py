from flask import Blueprint, render_template
import requests
from bs4 import BeautifulSoup
import pymysql

bp = Blueprint('teamrank', __name__, url_prefix='/rank')
viewRanking = 0  # 0: Team Ranking 1: POG Ranking


def getTeamRank():
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

    return r


def getPOGRank():
    url = "https://namu.wiki/w/2021%20LoL%20Champions%20Korea%20Spring"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ranking = soup.select_one(
        "#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(31) > div")
    pog_ranks = ranking.find_all('td')
    pog_data = []
    player = []
    p_cnt = 4

    for pog_rank in pog_ranks[7:]:
        pog_text = pog_rank.get_text()

        if '[' in pog_text[:5]:
            break
        if pog_text != '':
            player.append(pog_text)
            p_cnt -= 1

        if p_cnt == 0:
            pog_data.append(player)
            p_cnt = 4
            player = []

    for x in range(0, len(pog_data)):
        pname = pog_data[x][2]
        db = pymysql.connect(host='localhost', user='root', passwd='1234', db='lck', charset='utf8')
        cur = db.cursor()

        sql = "select liner from lckplayer where playername = '%s'"%(pname)
        cur.execute(sql)
        data = cur.fetchall()
        pog_data[x].append("../static/image/line/" + data[0][0] + ".png")
        # print("query : " , sql)
        # print(data[0][0])
        sql = "select team from lckplayer where playername = '%s'"%(pname)
        cur.execute(sql)
        data = cur.fetchall()
        pog_data[x].append("../static/image/team/" + data[0][0] + ".png")
        db.commit()
        cur.close()
        db.close()
    print(pog_data)
    return pog_data


r = getTeamRank()
pog_data = getPOGRank()


@bp.route('/')
def TeamRank():
    return render_template('rank.html', data_list=r, viewRanking=viewRanking)


@bp.route('/team')
def onTeamRank():
    viewRanking = 0
    return render_template('rank.html', data_list=r, viewRanking=viewRanking)


@bp.route('/pog')
def onPOGRank():
    viewRanking = 1
    return render_template('rank.html', pog_data=pog_data, viewRanking=viewRanking)
