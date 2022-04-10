from app.extensions import db, login_manager, bcrypt
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    account_created = db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    image_file = db.Column(db.String(20),
                           default='default.jpg')

    requests = db.relationship(
        'ExecutionRequest', backref='request_author', lazy='dynamic')

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class ExecutionRequest(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(), nullable=False)
    src = db.Column(db.String(), nullable=False)

    request_created = db.Column(db.DateTime, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    request_completed = db.Column(db.DateTime)

    returncode = db.Column(db.Integer)
    stdout = db.Column(db.String())
    stderr = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
