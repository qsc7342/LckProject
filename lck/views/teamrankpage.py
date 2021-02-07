from flask import Blueprint, render_template
import requests
from bs4 import BeautifulSoup

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

    return pog_data


@bp.route('/')
def TeamRank():
    r = getTeamRank()
    return render_template('rank.html', data_list=r, viewRanking=viewRanking)


@bp.route('/team', methods=['POST'])
def onTeamRank():
    r = getTeamRank()
    viewRanking = 0
    return render_template('rank.html', data_list=r, viewRanking=viewRanking)


@bp.route('/pog', methods=['POST'])
def onPOGRank():
    pog_data = getPOGRank()
    viewRanking = 1
    return render_template('rank.html', pog_data=pog_data, viewRanking=viewRanking)
