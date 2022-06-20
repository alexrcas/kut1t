def processAndSanitize(originalUrl):
    return checkForProtocol(originalUrl)


def checkForProtocol(originalUrl):
    if ('http://' in originalUrl) or ('https://' in originalUrl):
        return originalUrl
    return 'http://' + originalUrl