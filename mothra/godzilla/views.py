from flask import render_template, request, Blueprint, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from mothra import db
from mothra.models import User, Answer, Announcement, Hints
from mothra.forms import AnswerFillingForm, AnnounceForm, HintFillingForm
from mothra.views import classify
from datetime import datetime

godzilla = Blueprint('godzilla', __name__)

def godzilla_check():
    if current_user.user_type!='Godzilla':
        abort(403)

@godzilla.route('/admin_dash')
@login_required
def admin_dash():
    godzilla_check()
    return render_template('godzilla/admin_dash.html')


@godzilla.route('/corans', methods=['GET', 'POST'])
@login_required
def corans():
    godzilla_check()
    form=AnswerFillingForm()
    stages=Answer.query.all()
    if form.validate_on_submit():
        answer = Answer(stage=form.stage.data,
                    ans=form.ans.data)

        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('godzilla.corans', form=form, stages=stages))

    return render_template('godzilla/ans_filling.html', form=form, stages=stages)


@godzilla.route('/hints', methods=['GET', 'POST'])
@login_required
def hints():
    godzilla_check()
    form=HintFillingForm()
    stages=Hints.query.all()
    if form.validate_on_submit():
        hintt = Hints(stage=form.stage.data,
                    hint=form.hint.data)

        db.session.add(hintt)
        db.session.commit()
        return redirect(url_for('godzilla.hints', form=form, stages=stages))

    return render_template('godzilla/hint_filling.html', form=form, stages=stages)



@godzilla.route('/announce', methods=['GET','POST'])
@login_required
def announce():
    godzilla_check()
    form=AnnounceForm()
    if form.validate_on_submit():
        announcement=Announcement(message=form.message.data)
        db.session.add(announcement)
        db.session.commit()
        return redirect(url_for('godzilla.announce'))
    return render_template('godzilla/announce.html', form=form)


@godzilla.route('/all_users')
@login_required
def all_users():
    godzilla_check()
    users=User.query.order_by(User.id.asc()).all()
    return render_template('godzilla/users.html', users=users)
