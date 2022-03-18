

import json
from flask import Blueprint, flash, redirect, render_template, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required


from app import app, db
from .models import Trainer, Trainee, Gig, Enroll, GigSchema


import requests
import random


main = Blueprint('main', __name__)


weather = {
    "data": [
        {
            "day": "1/6/2019",
            "temperature": "23",
            "windspeed": "16",
            "event": "Sunny"
        },

    ]}


@main.route('/', methods=['GET'])
def index():
    gigs = Gig.query.all()

    gigs_schema = GigSchema(many=True)

    return jsonify(gigs_schema.dump(gigs))


@main.route('/weatherReport/')
def WeatherReport():
    global weather
    return jsonify([weather])


@main.route('/create_gig', methods=['POST'])
def create_gig():

    data = request.json

    title = data['title']
    price = data['price']
    duration = data['duration']
    category = data['category']
    trainer_id = data['trainerId']

    gig = Gig(title=title, price=price, duration=duration,
              category=category, trainer_id=trainer_id)

    db.session.add(gig)
    db.session.commit()

    return jsonify({'message': 'Gig created', 'status': 'success'})


@main.route('/book_gig/<gig_id>', methods=['GET', 'POST'])
@login_required
def book_gig(gig_id):

    if current_user.urole != "TRAINEE":
        flash('You are not authorized to book a gig')
        return redirect(url_for('main.index'))

    gig = Gig.query.filter_by(id=gig_id).first()

    if not gig:
        flash('Gig not found')
        return redirect(url_for('main.index'))

    # check if the user has already booked the gig
    if current_user.id in [enroll.trainee_id for enroll in gig.enrolls]:
        flash('You have already booked this gig')
        return redirect(url_for('main.index'))

    enroll = Enroll(gig_id=gig.id, trainee_id=current_user.id)

    db.session.add(enroll)
    db.session.commit()
    print(gig.enrolls)

    return redirect(url_for("main.index"))


@main.route('/display-gig/<gig_id>', methods=['GET'])
def display_gig(gig_id):

    gig = Gig.query.filter_by(id=gig_id).first()
    gig_category = gig.category

    url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{gig_category}"

    headers = {
        'x-rapidapi-host': "exercisedb.p.rapidapi.com",
        'x-rapidapi-key': "f50615db51msh1895e876776f30ep1045d3jsn5d2af3e0380f"
    }

    response = requests.request("GET", url, headers=headers)
    random_index = random.randint(0, 10)
    dis_gig = response.json()[random_index]

    return jsonify(dis_gig)
