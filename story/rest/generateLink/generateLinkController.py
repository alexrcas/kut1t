from flask import Blueprint, request
from service.linkService import getShortLink

generateLinkController = Blueprint('generateLinkController', __name__)
@generateLinkController.route('/short', methods = ['POST'])
def generateLink():
    url = request.get_json()['url']
    shortUrl = getShortLink(url)
    return {
            'url': f'http://kut.it/{shortUrl}'
        }