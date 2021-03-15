from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email
import email_validator

class AppForm(FlaskForm):
    name = StringField('Name', [ DataRequired() ])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    body = TextAreaField('Message', [ DataRequired(), Length(min=20, message=('Your message is not quite long enough, try again.')) ])
    submit = SubmitField('Send')