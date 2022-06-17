from flask import Blueprint, request
from util.encoder import toBase62

generateLinkController = Blueprint('generateLinkController', __name__)
@generateLinkController.route('/short', methods = ['POST'])
def generateLink():

    url = request.get_json()['url']
    #index = insertDB(url)
    index = len(url)
    shortUrl = toBase62(index)

    return {
            'url': f'http://kut.it/{shortUrl}'
        }