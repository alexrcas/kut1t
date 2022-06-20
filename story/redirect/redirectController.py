from flask import Blueprint, render_template
from service.linkService import getOriginalLink

redirectController = Blueprint('redirectController', __name__)
@redirectController.route('/<url>', methods = ['GET'])
def redirect(url):
    originalUrl = getOriginalLink(url)
    if len(originalUrl) == 0:
        return render_template('404.html')

    return render_template('redirect.html', urlToRedirect = originalUrl[0]['url'])