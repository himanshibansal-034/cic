from mothra import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime

start = datetime(2021, 4, 13)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    college_id = db.Column(db.String(64), unique=True, index=True)
    teamname = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    user_type=db.Column(db.String(128), default='Mothra')
    level = db.Column(db.Integer, default=0)
    upgrade_time = db.Column(db.DateTime)

    def __init__(self, college_id, teamname, password):
        self.college_id = college_id
        self.teamname = teamname
        self.password_hash = generate_password_hash(password)
        self.upgrade_time=datetime.now()

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"{self.id}, {self.college_id}, {self.teamname}"


class Attempts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stage = db.Column(db.Integer)
    atmpts = db.Column(db.Integer, default=1)
    user = db.relationship("User", backref="attempt", lazy=True)

    def __init__(self):
        self.uid = current_user.id
        self.stage = current_user.level+1


    def __repr__(self):
        return f"{self.id},{self.uid},{self.stage},{self.atmpts}"

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    stage = db.Column(db.Integer, nullable = False, unique=True)
    ans = db.Column(db.String)

    def __init__(self, stage, ans):
        self.stage = stage
        self.ans = ans

    def __repr__(self):
        return f"{self.id},{self.stage},{self.ans}"


class Hints(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    stage = db.Column(db.Integer, nullable = False, unique=True)
    hint = db.Column(db.String)

    def __init__(self, stage, hint):
        self.stage = stage
        self.hint = hint

    def __repr__(self):
        return f"{self.id},{self.stage},{self.hint}"


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String, nullable=False)

    def __init__(self, message):
        self.message=message

    def __repr__(self):
        return f"{self.id}, {self.message}"


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    uptime = db.Column(db.DateTime, nullable=False)
    user = db.relationship("User", backref="stats", lazy=True)

    def __init__(self):
        self.uid = current_user.id
        self.level = current_user.level
        self.uptime = datetime.now()

    def __repr__():
        return f"{self.uid}, {self.level}, {self.uptime}"
