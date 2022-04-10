import os


class Config:
    # Flask
    SECRET_KEY = 'mysecretkey'

    # Redis
    REDIS_URI = os.environ.get('REDIS_URI')

    # RabbitMQ
    RABBITMQ_URI = os.environ.get('RABBITMQ_URI')

    # Postgres
    POSTGRES_URI = os.environ.get('POSTGRES_URI')

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    """ SQLALCHEMY_DATABASE_URI = 'sqlite:///temp.db' """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SocketIO
    SOCKET_USE_BROKER = os.environ.get('SOCKET_USE_BROKER')
    SOCKETIO_BROKER_URI = os.environ.get('SOCKETIO_BROKER_URI')
    SOCKET_ASYNC_MODE = os.environ.get('SOCKET_ASYNC_MODE')

    # Celery
    CELERY_BROKER_URI = os.environ.get('CELERY_BROKER_URI')
    CELERY_USE_BACKEND = os.environ.get('CELERY_USE_BACKEND')
    CELERY_BACKEND_URI = os.environ.get('CELERY_BACKEND_URI')

    # Apllication
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    # Email
