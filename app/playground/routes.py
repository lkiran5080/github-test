from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from celery.result import AsyncResult

from app.extensions import db
from app.models import ExecutionRequest
from app.tasks import run


playground = Blueprint('playground', __name__)


@playground.route('/playground')
def get_playground():
    return render_template('playground.html', nonav=True)


@playground.route('/run', methods=['POST'])
def run_code():

    data = request.json

    lang = data['lang']
    src = data['src']

    # Create an entry in database
    req = ExecutionRequest(lang=lang, src=src, user_id=current_user.id)
    db.session.add(req)
    db.session.commit()

    # pass database id to celery task
    req_id = req.id
    task = run.apply_async(args=[req_id])

    return jsonify({"task_id": task.id}), 202


@playground.route('/status/<task_id>')
def get_status(task_id):

    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    
    print(result)
    
    return jsonify(result), 200

@playground.route('/langs')
def get_langs():
    return render_template('langs.html')

@playground.route('/showcase')
def get_showcase():
    return render_template('showcase.html')

@playground.route('/security')
def get_security():
    return render_template('security.html')

@playground.route('/home')
def get_user():
    
    past_requests = current_user.requests
    
    return render_template('home.html', past_requests=past_requests)

@playground.route('/result/<req_id>')
def get_result(req_id):
    
    result = ExecutionRequest.query.filter_by(id=req_id).get_or_404()
    
    return render_template('result.html', result = result)