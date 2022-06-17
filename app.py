from flask import Flask

from story.index.indexController import indexController
from story.rest.generateLink.generateLinkController import generateLinkController
from story.redirect.redirectController import redirectController


app = Flask(__name__, template_folder='web/templates',
    static_folder='web/static')
    
app.register_blueprint(indexController)
app.register_blueprint(generateLinkController)
app.register_blueprint(redirectController)

if __name__ == '__main__':
    app.run(debug=True)