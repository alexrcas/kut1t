from flask import Flask
import sqlite3

from story.index.indexController import indexController
from story.rest.generateLink.generateLinkController import generateLinkController
from story.redirect.redirectController import redirectController


connection = sqlite3.connect('database.db')
with open('schema.sql', 'r') as f:
    connection.executescript(f.read())
cur = connection.cursor()
connection.commit()
connection.close()



app = Flask(__name__, template_folder='web/templates',
    static_folder='web/static')
    
app.register_blueprint(indexController)
app.register_blueprint(generateLinkController)
app.register_blueprint(redirectController)

if __name__ == '__main__':
    app.run(debug=True)