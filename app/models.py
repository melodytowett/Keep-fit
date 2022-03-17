import profile
from flask_login import UserMixin
from importlib_metadata import email
from .import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from .import db

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first
    return user

class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String())
    # profile_pic = db.Column(db.String(),nullable=False)
    urole = db.Column(db.String(80))


class Trainer(User):
    __tablename__='trainers'
    phone_number = db.Column(db.String(15),unique=True)

class Trainee(User):
    __tablename__='trainees'
  
  
    # @property
    # def password(self):
    #     raise AttributeError('Password attribute cant be read')

    # @password.setter
    # def password(self, password):
    #     self.password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return f'User{self.username}'

 