from random import random
from util.encoder import toBase62, fromBase62
from model.urlDao import saveUrl, get, listUrls

def getShortLink(longUrl):
    row = saveUrl(longUrl)
    return toBase62(row['id'])


def getOriginalLink(shortUrl):
    index = fromBase62(shortUrl)
    return get(index)