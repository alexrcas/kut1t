from random import random
from util.encoder import toBase62, fromBase62
from model.urlDao import saveUrl, get
from service.sanitizerService import processAndSanitize


def getShortLink(longUrl):
    secureUrl = processAndSanitize(longUrl)
    row = saveUrl(secureUrl)
    return toBase62(row['id'])


def getOriginalLink(shortUrl):
    index = fromBase62(shortUrl)
    return get(index)