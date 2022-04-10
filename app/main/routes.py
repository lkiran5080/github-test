from flask import Blueprint, render_template, redirect, url_for

from app.tasks import add

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home')
def home():
    return redirect(url_for('playground.get_playground'))


@main.route('/test_celery')
def test_celery():
    task = add.delay(4, 4)
    return str(task.id)

