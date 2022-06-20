import validators
from flask import Blueprint, request, Response
from service.linkService import getShortLink


generateLinkController = Blueprint('generateLinkController', __name__)
@generateLinkController.route('/short', methods = ['POST'])
def generateLink():
    url = request.get_json()['url']

    if not validators.url(url):
        return {}, 400

    shortUrl = getShortLink(url)
    return { 'url': f'http://kut.it/{shortUrl}' }, 201