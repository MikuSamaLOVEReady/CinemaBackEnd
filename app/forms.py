from flask_wtf import Form, FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectField, IntegerField, PasswordField, SubmitField, \
    FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

from app.models import Tag
from app.models import User

def tag_query():
    return Tag.query


class UploadForm(FlaskForm):
    FilmName = StringField('FilmName', validators=[DataRequired()])
    Blurb = StringField('Blurb', validators=[DataRequired()])
    Certificate = StringField('Certificate', validators=[DataRequired()])
    Director = StringField('Director', validators=[DataRequired()])
    LeadActors = StringField('LeadActors', validators=[DataRequired()])
    FilmLength = StringField('FilmLength', validators=[DataRequired()])
    Genre = QuerySelectMultipleField('Genre', query_factory=tag_query, get_label='name', allow_blank=True)
    Ranking = IntegerField('Ranking', validators=[DataRequired()], default=100)
    file = FileField('File')


class SearchForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired()])


class TimeForm(FlaskForm):
    Date = DateField('Date', validators=[DataRequired()])


class FilmScheduleForm(Form):
    Room = StringField('Room', validators=[DataRequired()])
    Date = DateField('Date', validators=[DataRequired()])
    Time = StringField('Time', validators=[DataRequired()])
    Price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')#用户名是否重复

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')#邮箱是否重复


#订单提交表单
class OrderForm(Form):
    CustomerID = IntegerField('CustomerID', validators=[DataRequired()])
    SID = IntegerField('SID', validators=[DataRequired()])
    Seat = IntegerField('Seat', validators=[DataRequired()])
    DealTime = StringField('DealTime', validators=[DataRequired()])
