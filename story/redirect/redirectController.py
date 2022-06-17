import code
from flask import Blueprint, render_template

redirectController = Blueprint('redirectController', __name__)
@redirectController.route('/<url>')
def redirect(url):
    return render_template('redirect.html', urlToRedirect = url)