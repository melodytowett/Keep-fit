from flask import  render_template,redirect, request,url_for,flash
from flask_login import current_user, login_required, logout_user,login_user
from importlib_metadata import email
import werkzeug
from ..models import Trainer,Trainee,UserMixin
from .import auth
from ..import db
from werkzeug .security import generate_password_hash,check_password_hash
from .forms import TraineeRegistrationForm, TrainerRegistrationForm,TrainerLoginForm,TraineeLoginForm
# import uuid,jwt

# # from .. email import mail_message
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = TrainerRegistrationForm()
    # data  = request.get_json()
    if form.validate_on_submit():
        trainer = Trainer(email=form.email.data,username = form.username.data,phone_number = form.phone_number.data, password = form.password.data, urole='Trainer')   
        print(trainer.email,trainer.username,trainer.phone_number,trainer.password)
        db.session.add(trainer )
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = TrainerLoginForm()
    if login_form.validate_on_submit():
        trainer = Trainer.query.filter_by(email = login_form.email.data).first()
        print(trainer)
            # print(user.verify_password (login_form.password.data))
        if trainer is not None and trainer.verify_password(login_form.password.data): 
            
            login_user(trainer,login_form.remember_me.data)
            
            # return redirect(url_for('main.trainer'))
        return redirect(request.args.get('next') or url_for('main.index'))

    flash('Invalid username or Password')

    title = "Trainer login"
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/register_trainee',methods = ['GET','POST'])
def register_trainee():
    form = TraineeRegistrationForm()
    if form.validate_on_submit():
         trainee = Trainee(email=form.email.data,username = form.username.data,password = form.password.data,urole='Trainee')
         db.session.add(trainee)
         db.session.commit()
         return redirect(url_for('auth.login_trainee'))
    return render_template('auth/register_trainee.html',reg_form=form)


@auth.route('/login_trainee',methods=['GET','POST'])
def login_trainee():
    log_form= TraineeLoginForm()
    if log_form.validate_on_submit():
        trainee = Trainee.query.filter_by(email=log_form.email.data).first()
        print(trainee)
        if trainee is not None and trainee.verify_password(log_form.password.data):
            login_user(trainee,log_form.remember_me.data)
           
          
        return redirect(request.args.get('next')or url_for('main.index'))
    flash('Invalid username or password')

    return render_template('auth/login_trainee.html',log_form=log_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
