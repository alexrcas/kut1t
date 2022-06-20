import validators
from flask import Blueprint, request
from service.linkService import getShortLink


generateLinkController = Blueprint('generateLinkController', __name__)
@generateLinkController.route('/short', methods = ['POST'])
def generateLink():
    url = request.get_json()['url']

    if url is None:
        return {}, 400

    if not validators.url(url):
        return {}, 400

    shortUrl = getShortLink(url)
    return { 'url': f'http://kut.it/{shortUrl}', 'originalUrl': url }, 201