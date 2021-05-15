from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '31e8281c030ec4067a72fa8bdab7b098'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Database
db = SQLAlchemy(app)

from cafe import routes