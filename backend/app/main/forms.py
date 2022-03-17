from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    username = StringField('Enter your name',name="usrname", validators=[DataRequired()])
    email = StringField('Enter your email', validators=[Email()])
    message= TextAreaField('Enter your message', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Submit')
