
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String())
    profile_pic = db.Column(db.String(), nullable=False, default='default.svg')
    urole = db.Column(db.String(80))


class Trainer(User):
    phone_number = db.Column(db.String(15), unique=True)
    gigs = db.relationship('Gig', backref='trainer', passive_deletes=True)


class Trainee(User):

    gigs = db.relationship('Gig', backref='trainee', passive_deletes=True)


class Gig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Integer)
    duration = db.Column(db.String(100))
    category = db.Column(db.String(100))
    trainer_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)

    enrolls = db.relationship('Enroll', backref='gig', passive_deletes=True)


class Enroll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainee_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    gig_id = db.Column(db.Integer, db.ForeignKey(
        'gig.id', ondelete='CASCADE'), nullable=False)
