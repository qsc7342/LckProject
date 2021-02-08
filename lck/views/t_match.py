from flask import Blueprint, Flask, render_template, request, redirect ,url_for, flash, session
from flask_cors import CORS
import pymysql
import time
from datetime import datetime

bp = Blueprint('t_match', __name__, url_prefix='/t_match')

@bp.route('/')
def t_match():
    tm = datetime.today().strftime('%Y%m%d')
    time = int(tm)
    db = pymysql.connect(host='localhost', user='root', passwd='1234', db='lck', charset='utf8')
    cur = db.cursor()

    sql = "select mtime,team1,team2 from lckmatch where mdate = '%s'"%(time)
    cur.execute(sql)
    data = cur.fetchall()
    db.commit()
    cur.close()
    db.close()
    print(data)

    

    return render_template('t_match.html',data = data)
