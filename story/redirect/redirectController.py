from flask import Blueprint, render_template
from service.linkService import getOriginalLink

redirectController = Blueprint('redirectController', __name__)
@redirectController.route('/<url>', methods = ['GET'])
def redirect(url):
    originalUrl = getOriginalLink(url)
    return render_template('redirect.html', urlToRedirect = originalUrl['url'])