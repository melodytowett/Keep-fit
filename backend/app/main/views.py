from ..import mail
from email import message
from flask import render_template, flash, jsonify, request,redirect,url_for
from . import main
from flask_mail import Message, Mail
from .forms import ContactForm
from ..models import User
import os
import smtplib

mailing = os.environ.get("MAIL_USERNAME")

# Views
@main.route('/', methods = ['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    # title = 'Fire Fitness'
    # contact_form = ContactForm()
    # if contact_form.validate_on_submit():
    #     user = ContactForm.fetch(username = contact_form.username.data, email = contact_form.email.data, message = contact_form.message.data)
    #     msg = Message('Hello', sender = mailing, recipients = [mailing])
    #     msg.body = user.decode
    #     mail.send(msg)
    # #     return redirect(url_for('main.index'))
    contact_form = ContactForm()
    if request.method == "POST":
       # getting input 
       username = request.form.get("usrname")
       # getting input  
       email = request.form.get("email") 
       # getting input  
       message = request.form.get("message") 
       msg = Message('Hello', sender = mailing, recipients = [mailing])
       new_line = '\n'
       msg.body = f'The site has gotten a new subscriber.{new_line}Username: {username} {new_line}Email Address: {email} {new_line}Message Body: {message}' 
       mail.send(msg)
       return redirect(url_for('main.index'))
    return render_template("index.html", contact_form=contact_form)
    # contact_form = ContactForm()
    # if not contact_form.validate_on_submit():
    #     request.method == 'POST'
    #     req = request.form
    #     username = req.get(User(username = contact_form.username.data, email = contact_form.email.data, message = contact_form.message.data))
    #     # email = req.get["email"]
    #     # message = req.contact_form.get["message"]
    #     msg = Message('Hello', sender = mailing, recipients = [mailing])
    #     msg.body = f'{username}' 
    #     mail.send(msg)
    #     return render_template('index.html', contact_form=contact_form)
    # if request.method == 'POST':
    #     return redirect(url_for('main.index'))
    # # return "Sent"
    # return render_template('index.html', contact_form = contact_form)
    # user = User(username = contact_form.username.data, email = contact_form.email.data, message = contact_form.message.data)
        
    # mail_message = mail_message.split(Message(user, sender= mailing, recipients= mailing))
    # mail.send(mail_message)
        # return "Sent"
    # return render_template('index.html', contact_form = contact_form)

    # default_value = '0'
    # data = request.form.get('input_name', default_value)
    # msg = Message('Hello', sender = mailing, recipients = [mailing])
    # msg.body = "username = contact_form.username.data, email = contact_form.email.data, message = contact_form.message.data"
    # mail.send(msg)
    # # return "Sent"
    # return render_template('index.html', contact_form = contact_form)