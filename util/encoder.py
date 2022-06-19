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


def fromBase62(string):
    total = 0
    exp = 0
    for character in string[::-1]:
        position = ALPHABET.index(character)
        total += position * (BASE ** exp)
        exp = exp + 1
    return total