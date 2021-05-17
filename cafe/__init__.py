from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 

# Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '31e8281c030ec4067a72fa8bdab7b098'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Database
db = SQLAlchemy(app)
# Bcrypt
bcrypt = Bcrypt(app)
# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from cafe import routes