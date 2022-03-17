from distutils.log import error
from flask import render_template
from .import main

@main.app_errorhandler(404)
def four_04(error):
    """
    Function to render the 404 error page_
    """
    return render_template('404.html'), 404