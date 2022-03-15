from calendar import c
from enum import unique
from errno import EMLINK
from tokenize import String
from flask_login import UserMixin
from importlib_metadata import email
from .import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from .import db


@login_manager.user_loader
def load_user(id):
    return Trainer.query.get(int(id))

class Trainer(UserMixin,db.Model):
    __tablename__='trainers'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True)
    phone_number = db.Column(db.Integer,unique=True)
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('Password attrinute cant be read')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'Trainer{self.username}'

class Trainee(UserMixin,db.Model):
    __tablename__='trainee'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True)
    pass_secure = db.Column(db.String(255))
   
    @property
    def password(self):
        raise AttributeError('Password attrinute cant be read')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'Trainee{self.username}'
