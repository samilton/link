from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
Config(app)

app.config['SQLALCHEMY_DATABASE_URI'] = app.config['LINK']['database']['uri']
db = SQLAlchemy(app)

from app import models
from app import views
