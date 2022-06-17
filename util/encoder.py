import math

ALPHABET = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
BASE = 62

def toBase62(number):

    if (number == 0):
        return ALPHABET[0]

    results = []
    while number > 0:
        module, number = getModuleAndResult(number)
        results.insert(0, module)
    
    encodedResults = list(map(lambda result : ALPHABET[result], results))
    return ''.join(encodedResults)


def getModuleAndResult(number):
    return number % BASE, math.floor(number / BASE)