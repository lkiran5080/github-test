""" from dotenv import load_dotenv
load_dotenv('local.env') """

from flask import Flask

from app.config import Config
from app.extensions import bcrypt, db, login_manager, migrate
from celery import Celery
import os

celery = Celery(__name__, broker=os.environ.get(
    'CELERY_BROKER_URI'), backend=os.environ.get('CELERY_BACKEND_URI'))

#print(os.environ.get('CELERY_BROKER_URI'))


def create_app(config_file=Config):

    app = Flask(__name__)
    app.config.from_object(config_file)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    
    # import blueprints
    from app.main.routes import main
    from app.users.routes import users
    from app.playground.routes import playground
    
    # register blueprints
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(playground)
    
    # configure loggers
    
    return app
