from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL',
                                               default='postgresql://postgres@localhost:5432/loadstone')
db = SQLAlchemy(app)

import api.views
