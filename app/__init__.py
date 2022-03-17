from distutils.command.upload import upload
from webbrowser import get
from flask import Flask,app
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
# from flask__uploads import UploadSet, configure_uploads,IMAGES


# @login_manager.user_loader
# def load_user(user_id):
#     return get_user(user_id)
bootstrap = Bootstrap()
db = SQLAlchemy()
# photos = uploadSet('photos',IMAGES)

login_manager=LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view='auth.login'

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY']='f869f86f2c98249f18e72b34f94768f1'
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://moringa:1234@localhost/fitness'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
  
    login_manager.init_app(app)
    

    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    # Will add the views and forms

    return app