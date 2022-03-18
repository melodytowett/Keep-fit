from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow


from .config import config_options

UPLOAD_FOLDER = 'app/static/img'


app = Flask(__name__)

app.config.from_object(config_options['development'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
ma = Marshmallow(app)

from .models import User


def create_app():
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is the primary key, we use it to query
        return User.query.get(int(user_id))

    # blueprint for auth parts of the app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of the app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
