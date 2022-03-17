from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required


from app import app, db
from .models import Trainer, Trainee, Gig, Enroll


import requests
import random


main = Blueprint('main', __name__)


@main.route('/')
def index():
    gigs = Gig.query.all()
    return render_template('index.html', gigs=gigs)


@main.route('/create_gig', methods=['GET', 'POST'])
@login_required
def create_gig():

    if current_user.urole != "TRAINER":
        flash('You are not authorized to create a gig')
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        duration = request.form.get('duration')
        category = request.form.get('category')
        trainer_id = current_user.id

        gig = Gig(title=title, price=price, duration=duration,
                  category=category, trainer_id=trainer_id)

        db.session.add(gig)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template('trainer/create_gig.html', )


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


@main.route('/view_gig/<gig_id>', methods=['GET', 'POST'])
def view_gig(gig_id):

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

    return render_template('view_gig.html', dis_gig=dis_gig)
