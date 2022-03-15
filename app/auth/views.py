from flask import flash, render_template,redirect, request,url_for
from flask_login import login_required, logout_user,login_user
from ..models import Trainer,Trainee
from .import auth
from ..import db
from .forms import TraineeRegistrationForm, TrainerRegistrationForm,TrainerLoginForm,TraineeLoginForm

# from .. email import mail_message
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = TrainerRegistrationForm()
    if form.validate_on_submit():
        user = Trainer(email=form.email.data,username = form.username.data,phone_number = form.phone_number.data, password = form.password.data)   
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = TrainerLoginForm()
    if login_form.validate_on_submit():
        user = Trainer.query.filter_by(email = login_form.email.data).first()
            # print(user.verify_password (login_form.password.data))
        if user is not None and user.verify_password(login_form.password.data): 
            login_user(user,login_form.remember_me.data)
            # return redirect(url_for('main.trainer'))
        return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Trainer login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register_trainee',methods = ['GET','POST'])
def register_trainee():
    form = TraineeRegistrationForm()
    if form.validate_on_submit():
         user = Trainee(email=form.email.data,username = form.username.data,password = form.password.data)
         db.session.add(user)
         db.session.commit()
         return redirect(url_for('auth.login'))
    return render_template('auth/register_trainee.html',reg_form=form)


@auth.route('/login_trainee',methods=['GET','POST'])
def login_trainee():
    log_form= TraineeLoginForm()
    if log_form.validate_on_submit():
        user = Trainee.query.filter_by(email=log_form.email.data).first()
        if user is not None and user.verify_password(log_form.password.data):
            login_user(user,log_form.remember_me.data)
            
        return redirect(request.args.get('next')or url_for('main.index'))
        flash('Invalid username or password')

    return render_template('auth/login_trainee.html',log_form=log_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))