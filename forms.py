from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, validators, IntegerField, RadioField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email
import email_validator
from datetime import date

class AppForm(FlaskForm):
    '''
    Sample job application form fields and labels.
    '''
    position = SelectField('What position are you applying for?', [DataRequired()], choices=[('acc', 'Accounting Manager'), ('dev', 'Junior Software Engineer (5+ years exp required)'), ('koopa', 'Koopa Troopa'), ('astmgr', 'Assistant to the Regional Manager')])
    fname = StringField('First Name', [ DataRequired() ])
    lname = StringField('Last Name', [ DataRequired() ])
    email = StringField('Email', [validators.DataRequired(), Email()])
    street = StringField('Street Address', [ DataRequired() ])
    city = StringField('City', [DataRequired()])
    zcode = IntegerField('Zip Code', [DataRequired(), Length(min=5, message=('Please enter a valid, 5 digit zip code.')) ])
    salary = StringField('Requested Salary ($ Per Year)', [DataRequired()])
    experience = TextAreaField('Experience from the last 16 years (no resumes accepted)', [DataRequired()])
    work = RadioField('Are you willing to work 90 hour weeks?', [DataRequired()], choices=[('Yes','yes'),('Also Yes','yes2')])
    sue = BooleanField('If you get hurt on the job, you can\'t sue us.', [DataRequired()])
    data = BooleanField('We will probably collect your data and you should allow us to do it.', [DataRequired()])
    startdate = DateField('GREAT! When can you start?', default = date.today)
    submit = SubmitField('Send')