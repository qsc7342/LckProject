from app import db

class lckplayer(db.Model):
    name = db.Column(db.Text(), primary_key=True)
    team = db.Column(db.Text(), nullable = False)
    line = db.Column(db.Text(), nullable = False)

class lckmatch(db.Model):
    mdate = db.Column(db.Text(), primary_key=True)
    mtime = db.Column(db.Text(), primary_key=True)
    team1 = db.Column(db.Text(), nullable = False)
    team2 = db.Column(db.Text(), nullable = False)
    