from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from constants import dropdown


class LdapForm(FlaskForm):
    company = StringField('Company: ', validators=[Length(max=30)])
    username = StringField('Username: ', validators=[Length(max=30)])
    firstname = StringField('First Name: ', validators=[Length(max=30)])
    surname = StringField('Surname: ', validators=[Length(max=30)])
    password = PasswordField('Password: ', validators=[Length(min=7, max=16)])
    dropdown = SelectField('Function: ', choices=dropdown)
    submit = SubmitField('submit')
