from urllib.parse import quote

def processAndSanitize(originalUrl):
    return quote(originalUrl, safe = '/:?&')