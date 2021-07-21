from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, NumberRange
from wtforms import ValidationError
from wtforms.fields.html5 import DecimalRangeField
from mothra.models import User

class LoginForm(FlaskForm):
    teamname = StringField('Team Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    college_id = IntegerField('College ID', validators=[DataRequired()])
    teamname = StringField('Team Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message="Passwords must Match!")])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_college_id(self,college_id):
        if User.query.filter_by(college_id=self.college_id.data).first():
            raise ValidationError("College ID already registered!")

    def validate_teamname(self,teamname):
        if User.query.filter_by(teamname=self.teamname.data).first():
            raise ValidationError("Team Name already registered!")


class AnswerFillingForm(FlaskForm):
    stage = IntegerField('Stage', validators=[DataRequired()])
    ans = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField('Submit')


class HintFillingForm(FlaskForm):
    stage = IntegerField('Stage', validators=[DataRequired()])
    hint = StringField('Hint', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SubmissionForm(FlaskForm):
    ans = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AnnounceForm(FlaskForm):
    message = StringField('Announcement', validators=[DataRequired()])
    submit = SubmitField('Submit')
