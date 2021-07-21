from flask import render_template, request, Blueprint, redirect, url_for, flash, abort
from mothra import app, db, start, end
from flask_login import login_user, login_required, logout_user, current_user
from mothra.models import User, Announcement
from mothra.forms import LoginForm, RegistrationForm, SubmissionForm, AnswerFillingForm
from datetime import datetime

# COMMON FUNCTIONS AND OBJECTS

classify=['born','noob','unknown','amateur','average','working','famous','creator','wip']

# CONTEXT PROCESSOR


@app.context_processor
def inject_level():
    def getlev():
        if current_user.is_authenticated:
            lev=classify[current_user.level]
        else:
            lev=''
        return lev

    def clss():
        return classify[1:current_user.level+2]

    def show():
        return classify

    return dict(getlev=getlev, clss=clss, show=show, time=datetime.now(), start=start, end=end)



# GENERAL VIEWS

@app.route('/')
def index():
    announcement=Announcement.query.order_by(Announcement.id.desc()).first()
    return render_template('home.html', announcement=announcement)

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(college_id=form.college_id.data,
                    teamname=form.teamname.data,
                    password=form.password.data
                    )

        db.session.add(user)
        db.session.commit()
        flash("Thank you for registering " +form.teamname.data+ ". Please login.")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    form=LoginForm()

    if form.validate_on_submit():
        user=User.query.filter_by(teamname=form.teamname.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                next=request.args.get('next')
                if next==None or not not next[0]=='/':
                    next=url_for('index')
                flash("Login Successful")
                return redirect(next)

            else:
                flash("Password is incorrect.")

        else:
            flash("Team Name does not exist.")
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/leaderboard')
def leaderboard():
    users=User.query.filter_by(user_type="Mothra").order_by(User.level.desc(), User.upgrade_time.asc()).all()
    return render_template('leaderboard.html', users=users)

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/hunting')
@login_required
def hunting():
    le=current_user.level
    return redirect(url_for('challenges.'+classify[le+1]))

@app.route('/announcements')
def announcements():
    ancmts=Announcement.query.all()
    ancmts.reverse()
    return render_template('announcements.html', ancmts=ancmts)
