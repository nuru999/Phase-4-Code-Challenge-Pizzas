
import os
from flask import Flask, make_response,jsonify
from flask_migrate import Migrate
# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# create both app and api instances
app = Flask(__name__)
CORS(app)
# api = Api(app)




app.config['SECRET_KEY'] = 'a16e4b678a12af3ac6df0b0d9b40db31'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizzaria.db"
# initialize the app with the extension

from  api import routes
from api.models import db

migrate = Migrate(app, db)
db.init_app(app)