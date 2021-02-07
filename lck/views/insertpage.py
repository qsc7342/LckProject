from flask import Blueprint, render_template, request
from app import db
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from schema import lckplayer
bp = Blueprint('insert', __name__, url_prefix='/insert')

@bp.route('/')
def MainPage():
	return render_template('insertpage.html')

@bp.route('/create/', methods=('POST',))
def create():
    name = request.form['name']
    team = request.form['team']
    line = request.form['line']
    newplayer = lckplayer(name = name, team = team, line = line)
    db.session.add(newplayer)
    db.session.commit()
    return render_template('insertpage.html')