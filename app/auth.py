
from urllib.parse import uses_relative
from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

from .models import Trainer, Trainee, Gig


auth = Blueprint('auth', __name__)


@auth.route('/trainer/signup', methods=['GET', 'POST'])
def trainer_signup():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        username = request.form.get('username').lower()
        password = request.form.get('password')
        phone_number = request.form.get('phone_number')

        # Lookup if email or username exists
        user_email = Trainer.query.filter_by(email=email).first()
        user_username = Trainer.query.filter_by(username=username).first()

        if user_email:
            flash('Email already exists')
            return render_template('trainer/signup.html')
        if user_username:
            flash('Username already taken')
            return render_template('trainer/signup.html')

        trainer = Trainer(email=email, username=username, password=generate_password_hash(
            password), phone_number=phone_number, urole='TRAINER')

        db.session.add(trainer)
        db.session.commit()

        return render_template('trainer/login.html')

    return render_template('trainer/signup.html')


@auth.route('/trainer/login', methods=['GET', 'POST'])
def trainer_login():
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        trainer = Trainer.query.filter_by(username=username).first()

        if not trainer:
            flash('Trainer with that username does not exist')
            return render_template('trainer/login.html')
        if not check_password_hash(trainer.password, password):
            flash('Incorect password.')
            return render_template('trainer/login.html')

        # if the above check passes then...
        login_user(trainer, remember=remember)
        return render_template('trainer/profile.html')

    return render_template('/trainer/login.html')


@auth.route('/trainee/signup', methods=['GET', 'POST'])
def trainee_signup():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        username = request.form.get('username').lower()
        password = request.form.get('password')

        # Lookup if email or username exists
        user_email = Trainee.query.filter_by(email=email).first()
        user_username = Trainee.query.filter_by(username=username).first()

        if user_email:
            flash('Email already exists')
            return render_template('trainee/signup.html')
        if user_username:
            flash('Username already taken')
            return render_template('trainee/signup.html')

        trainee = Trainee(email=email, username=username, password=generate_password_hash(
            password), urole='TRAINEE')

        db.session.add(trainee)
        db.session.commit()
        return render_template('trainee/login.html')

    return render_template('trainee/signup.html')


@auth.route('/trainee/login', methods=['GET', 'POST'])
def trainee_login():
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        trainee = Trainee.query.filter_by(username=username).first()

        if not trainee:
            flash('Trainee with that username does not exist')
            return render_template('trainee/login.html')
        if not check_password_hash(trainee.password, password):
            flash('Incorect password.')
            return render_template('trainee/login.html')

        # if the above check passes then...
        login_user(trainee, remember=remember)
        return render_template('trainee/profile.html')

    return render_template('/trainee/login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))
