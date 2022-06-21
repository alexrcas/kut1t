import validators
from flask import Blueprint, request
from service.linkService import getShortLink


generateLinkController = Blueprint('generateLinkController', __name__)
@generateLinkController.route('/short', methods = ['POST'])
def generateLink():
    print('#GenerateLinkController: ' + request.get_json()['url'])
    url = request.get_json()['url']

    if url is None:
        return {}, 400

    if not validators.url(url):
        return {}, 400

    shortUrl = getShortLink(url)
    return { 'url': f'https://kut1t.herokuapp.com/{shortUrl}', 'originalUrl': url }, 201