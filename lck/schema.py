from app import db

class lckplayer(db.Model):
    name = db.Column(db.Text(), primary_key=True)
    team = db.Column(db.Text(), nullable = False)
    line = db.Column(db.Text(), nullable = False)