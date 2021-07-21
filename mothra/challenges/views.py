from flask import render_template, request, Blueprint, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from mothra import db, start, end
from mothra.models import User, Attempts, Answer, Announcement, Stats, Hints
from mothra.forms import SubmissionForm
from mothra.views import classify
from datetime import datetime, timedelta
import math


challenges = Blueprint('challenges', __name__)

# SUBMISSION HANDLING

def sub(form, attemp):
    now=datetime.now()
    if now>end:
        flash("The submission time is over. No new answers will be accepted.")
        return redirect(url_for("index"))
    att=Attempts.query.filter_by(uid=current_user.id, stage= current_user.level+1).first()
    if att:
        if att.atmpts>=attemp:
            att.atmpts+=1
        else:
            att.atmpts+=1
    else:
        atmpt=Attempts()
        db.session.add(atmpt)
    ans=form.ans.data
    corans=Answer.query.filter_by(stage=current_user.level+1).first()
    if ans!=corans.ans:
        message = "Oops! Your Submission for the "+classify[current_user.level+1] + " upgrade on "+now.strftime("%d %b %Y at %I:%M %p")+" has been rejected because your answer was incorrect."
        le=current_user.level
        next='challenges.'+classify[le+1]

    else:
        current_user.level+=1
        current_user.upgrade_time=datetime.now()
        stat = Stats()
        db.session.add(stat)
        message = "Your Submission for the "+classify[current_user.level] + " upgrade on "+now.strftime("%d %b %Y at %I:%M %p")+" is correct. You have been upgraded to " + classify[current_user.level]
        le=current_user.level
        next='challenges.'+classify[le+1]

    flash(message)
    db.session.commit()
    return next


def get_hint(stage):
    db_hint = Hints.query.filter_by(stage=stage).first()
    diff =datetime.now() - current_user.upgrade_time
    mins = 60 - math.floor(diff.total_seconds()/60)

    if diff<timedelta(hours=1) :
        hint = "You need to wait for another " + str(mins) + " minutes before you can get the hint."
    else :
        hint = db_hint.hint

    return hint



#CHALLENGE ROUTES

@challenges.route('/noob', methods=['GET', 'POST'])
@login_required
def noob():
    if datetime.now()<start and current_user.user_type!="Godzilla":
        flash("Event has not yet started.")
        return redirect(url_for("index"))
    if current_user.level>0 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=1, uid=current_user.id).first()
        return render_template('challenges/chal_1.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(uid=current_user.id, stage=1).first()
        hint = get_hint(1)
        if form.validate_on_submit():
            next=sub(form, att)
            return redirect(url_for(next))

        return render_template('challenges/chal_1.html', form=form, attempts=attempts, att=att, hint=hint)

@challenges.route('/unknown', methods=['GET', 'POST'])
@login_required
def unknown():
    if current_user.level<1:
        abort(403)
    elif current_user.level>1 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=2, uid=current_user.id).first()
        return render_template('challenges/chal_2.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(uid=current_user.id, stage=2).first()
        hint = get_hint(2)
        if form.validate_on_submit():
            next=sub(form, att)
            return redirect(url_for(next))

        return render_template('challenges/chal_2.html', form=form, attempts=attempts, att=att, hint=hint)

@challenges.route('/amateur', methods=['GET', 'POST'])
@login_required
def amateur():
    if current_user.level<2:
        abort(403)

    elif current_user.level>2 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=3, uid=current_user.id).first()
        return render_template('challenges/chal_3.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(uid=current_user.id, stage=3).first()
        hint = get_hint(3)
        if form.validate_on_submit():
            next=sub(form, att)
            return redirect(url_for(next))

        return render_template('challenges/chal_3.html', form=form, attempts=attempts, att=att, hint=hint)

@challenges.route('/average', methods=['GET', 'POST'])
@login_required
def average():
    if current_user.level<3:
        abort(403)

    elif current_user.level>3 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=4, uid=current_user.id).first()
        return render_template('challenges/chal_4.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(uid=current_user.id, stage=4).first()
        hint = get_hint(4)
        if form.validate_on_submit():
            next=sub(form, att)
            return redirect(url_for(next))

        return render_template('challenges/chal_4.html', form=form, attempts=attempts, att=att, hint=hint)

@challenges.route('/working', methods=['GET', 'POST'])
@login_required
def working():
    if current_user.level<4:
        abort(403)

    elif current_user.level>4 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=5, uid=current_user.id).first()
        return render_template('challenges/chal_5.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(uid=current_user.id, stage=5).first()
        hint = get_hint(5)
        if form.validate_on_submit():
            next=sub(form, att)
            return redirect(url_for(next))

        return render_template('challenges/chal_5.html', form=form, attempts=attempts, att=att, hint=hint)

@challenges.route('/famous', methods=['GET', 'POST'])
@login_required
def famous():
    if current_user.level<5:
        abort(403)

    elif current_user.level>5 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=6, uid=current_user.id).first()
        return render_template('challenges/chal_6.html', stats=stats)
    else:
        form=SubmissionForm()
        att=3
        attempts=Attempts.query.filter_by(uid=current_user.id, stage=6).first()
        hint = get_hint(6)
        if form.validate_on_submit():
            next=sub(form, att)
            return redirect(url_for(next))

        return render_template('challenges/chal_6.html', form=form, attempts=attempts, att=att, hint=hint)

@challenges.route('/creator', methods=['GET', 'POST'])
@login_required
def creator():
    if current_user.level<6:
        abort(403)

    elif current_user.level>6 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=7, uid=current_user.id).first()
        return render_template('challenges/chal_7.html', stats=stats)
    else:
        form=SubmissionForm()
        att=3
        attempts=Attempts.query.filter_by(uid=current_user.id, stage=7).first()
        hint = get_hint(7)
        if form.validate_on_submit():
            next=sub(form, att)
            return redirect(url_for(next))

        return render_template('challenges/chal_7.html', form=form, attempts=attempts, att=att, hint=hint)

@challenges.route('/wip', methods=['GET', 'POST'])
@login_required
def wip():
    return render_template('wip.html')
