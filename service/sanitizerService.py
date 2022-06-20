from urllib.parse import quote

def processAndSanitize(originalUrl):
    sanitizedUrl = sanitize(originalUrl)
    return checkForProtocol(sanitizedUrl)


def checkForProtocol(sanitizedUrl):
    if ('http://' in sanitizedUrl) or ('https://' in sanitizedUrl):
        return sanitizedUrl
    return 'http://' + sanitizedUrl


def sanitize(originalUrl):
    return quote(originalUrl, safe = '/:?&')