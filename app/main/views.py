from flask import redirect, render_template
from . import main



@main.route('/')
def index():

    message ='Melo you are the best developer just believe in yourself'
    return render_template('index.html',message=message)