from wsgiref.validate import validator
from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import ValidationError
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError,IntegerField
from wtforms .validators import DataRequired,Email,EqualTo

from..models import Trainer,Trainee

class TrainerRegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    phone_number = IntegerField('indicate phone number',validators=[DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')


    def validate_email(self, data_field):
        if Trainer.query.filter_by(email=data_field.data).first():
            raise ValidationError('That email is already used')

    def validate_phone_number(self, data_field):
        if Trainer.query.filter_by(phone_number=data_field.data).first():
            raise ValidationError("phone number already exist")


class TrainerLoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me= BooleanField("Remember me")
    submit = SubmitField('Login')

class TraineeRegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')



    def validate_email(self, data_field):
        if Trainee.query.filter_by(email=data_field.data).first():
            raise ValidationError('That email is already used')

    def validate_username(self, data_field):
        if Trainee.query.filter_by(username=data_field.data).first():
            raise ValidationError("username already exist")


class TraineeLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me= BooleanField("Remember me")
    submit = SubmitField('Login')



