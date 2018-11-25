from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.db_uri()
db = SQLAlchemy(app)

from app.routes import *
