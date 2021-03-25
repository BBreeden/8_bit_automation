from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, validators, IntegerField, RadioField, BooleanField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, NumberRange
import email_validator
from datetime import date

class AppForm(FlaskForm):
    '''
    Sample job application form fields and labels.
    '''
    position = SelectField('What position are you applying for?', [DataRequired()], choices=[('Accounting Manager', 'Accounting Manager'), ('Junior Software Engineer', 'Junior Software Engineer (5+ years exp required)'), ('Koopa Troopa', 'Koopa Troopa'), ('Assistant to the Regional Manager', 'Assistant to the Regional Manager')])
    branch = SelectField('Please select a branch:', choices=[('Scranton, PA', 'Scranton, PA'), ('Akron, OH', 'Akron, OH'), ('Albany, NY', 'Albany, NY'), ('Nashua, NH', 'Nashua, NH'), ('New York City - Corporate HQ', 'New York City - Corporate HQ'), ('Rochester, NY', 'Rochester, NY'), ('Utica, NY', 'Utica, NY'), ('Syracuse, NY', 'Syracuse, NY')])
    fname = StringField('First Name', [ DataRequired() ])
    lname = StringField('Last Name', [ DataRequired() ])
    email = StringField('Email', [DataRequired(), Email(message='Invalid email address.')])
    street = StringField('Street Address', [ DataRequired() ])
    city = StringField('City', [DataRequired()])
    zcode = IntegerField('Zip Code', [DataRequired(), NumberRange(min=10000, max=99999, message='Invalid zip code, enter a 5 didit US zip code.')] )
    salary = StringField('Requested Salary ($ Per Year)', [DataRequired()])
    experience = TextAreaField('Experience from the last 16 years (no resumes accepted)', [DataRequired()])
    work = RadioField('Are you willing to work 90 hour weeks?', [DataRequired()], choices=[('Yes','yes'),('Also Yes','yes2')])
    sue = BooleanField('If you get hurt on the job, you can\'t sue us.', [DataRequired()])
    data = BooleanField('We will probably collect your data and you should allow us to do it.', [DataRequired()])
    startdate = DateField('When can you start?')
    submit = SubmitField('Send')