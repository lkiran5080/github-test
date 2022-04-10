import os
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

""" 
if os.environ.get('SOCKETIO_BROKER_URI'):
    socketio = SocketIO(message_queue=os.environ.get('SOCKETIO_BROKER_URI'))
else:
    socketio = SocketIO() """
