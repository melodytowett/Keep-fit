

from flask import Blueprint, redirect, url_for, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
import json

from .models import Trainer, Trainee, Gig


auth = Blueprint('auth', __name__)


@auth.route('/trainer/signup', methods=['GET', 'POST'])
def trainer_signup():

    data = request.json

    email = data['email']
    username = data['username']
    phone_number = data['phone_number']
    password = data['password']

    # Lookup if email or username exists
    user_email = Trainer.query.filter_by(email=email).first()
    user_username = Trainer.query.filter_by(username=username).first()

    if user_email:
        return jsonify({'message': 'Email already exists', 'status': 'error'})
    if user_username:
        return jsonify({'message': 'Username already taken', 'status': 'error'})

    trainer = Trainer(email=email, username=username, password=generate_password_hash(
        password), phone_number=phone_number, urole='TRAINER')

    db.session.add(trainer)
    db.session.commit()

    return jsonify({'message': 'Trainer created', 'status': 'success'})


@auth.route('/trainer/login', methods=['POST'])
def trainer_login():
    data = request.json

    username = data['username']
    password = data['password']

    trainer = Trainer.query.filter_by(username=username).first()

    if not trainer:
        return jsonify({'message': 'No such user', 'status': 'error'})
    if not check_password_hash(trainer.password, password):
        return jsonify({'message': 'Wrong password', 'status': 'error'})

    # if the above check passes then...
    login_user(trainer)
    user_id = current_user.id
    return jsonify({'message': 'Logged in', 'status': 'success', 'user_id': user_id})


@auth.route('/trainee/signup', methods=['POST'])
def trainee_signup():
    data = request.json

    email = data['email']
    username = data['username']
    password = data['password']

    # Lookup if email or username exists
    user_email = Trainee.query.filter_by(email=email).first()
    user_username = Trainee.query.filter_by(username=username).first()

    if user_email:
        return jsonify({'message': 'Email already exists', 'status': 'error'})
    if user_username:
        return jsonify({'message': 'Username already taken', 'status': 'error'})

    trainee = Trainee(email=email, username=username, password=generate_password_hash(
        password), urole='TRAINEE')

    db.session.add(trainee)
    db.session.commit()

    return jsonify({'message': 'Trainee created', 'status': 'success'})


@auth.route('/trainee/login', methods=['POST'])
def trainee_login():
    data = request.json

    username = data['username']
    password = data['password']

    trainee = Trainee.query.filter_by(username=username).first()

    if not trainee:
        print('Trainee with that username does not exist')
        return jsonify({'message': 'Trainee with that username does not exist', 'status': 'error'})
    if not check_password_hash(trainee.password, password):
        print('Incorect password.')
        return jsonify({'message': 'Incorect password.', 'status': 'error'})

    # if the above check passes then...
    login_user(trainee)

    return jsonify({'message': 'Trainee logged in', 'status': 'success', })


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))
