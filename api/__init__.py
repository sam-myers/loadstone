from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL', default='sqlite://')
db = SQLAlchemy(app)

import api.views
