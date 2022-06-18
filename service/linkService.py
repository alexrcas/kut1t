from random import random
import math
from util.encoder import toBase62

def getShortLink(longUrl):
    #insertar en BD
    #index = insert(db, longUrl)
    # return toBase62(index)
    index = math.floor(random() * 10000000)
    return toBase62(index)
