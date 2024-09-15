import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from .dash import init_dash
from .db import db

load_dotenv()

# Initialize Flask app
app = Flask(__name__)
migrate = Migrate(app, db)

# Load configurations
API_KEY = os.getenv('API_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init database
db.init_app(app)

# Initialize Dash app
init_dash(app)

from . import views
