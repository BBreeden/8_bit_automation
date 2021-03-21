from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, validators, IntegerField, RadioField, BooleanField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class AppForm(FlaskForm):
    fname = StringField('First Name', [ DataRequired() ])
    lname = StringField('Last Name', [ DataRequired() ])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    street = StringField('Street Address', [ DataRequired() ])
    city = StringField('City', [DataRequired()])
    zcode = IntegerField('Zip Code', [DataRequired(), Length(min=5, max=5, message=('Please enter a valid, 5 digit zip code.')) ])
    experience = TextAreaField('Experience from the last 16 years (no resumes accepted)', [DataRequired()])
    salary = StringField('Requested Salary', [DataRequired()])
    work = RadioField('Are you willing to work 90 hour weeks?', [DataRequired()], choices=[('Yes','yes'),('Also Yes','yes2')])
    boss = BooleanField('If you get hurt on the job, you can\'t sue us.', [DataRequired()])
    mario = BooleanField('If an Italian plumber shows up and starts making a mess, do you agree to clean it up?', [DataRequired()])
    submit = SubmitField('Send')