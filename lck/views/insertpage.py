from flask import Blueprint, render_template, request
from app import db
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from schema import lckmatch
bp = Blueprint('insert', __name__, url_prefix='/insert')

@bp.route('/')
def MainPage():
	return render_template('insertpage.html')

@bp.route('/create/', methods=('POST',))
def create():
    mdate = request.form['mdate']
    mtime = request.form['mtime']
    team1 = request.form['team1']
    team2 = request.form['team2']
    newmatch = lckmatch(mdate = mdate, mtime = mtime, team1 = team1, team2 = team2)
    db.session.add(newmatch)
    db.session.commit()
    return render_template('insertpage.html')