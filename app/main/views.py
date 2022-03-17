from flask import redirect, render_template,abort
from . import main
from ..models import Trainer
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@main.route('/' ,methods=['GET'])

def index():

    message ='Melo you are the best developer just believe in yourself'
    return render_template('index.html',message=message)


