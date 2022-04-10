import os

from app import create_app, celery
from celery import Celery
from .runners import py_runner, c_runner, cpp_runner, js_runner
from app.extensions import db
from app.models import ExecutionRequest
from datetime import datetime
import uuid




#celery.conf.broker_url = os.environ.get('CELERY_BROKER_URI')
#celery.conf.result_backend = os.environ.get('CELERY_BACKEND_URI')
celery.conf.task_time_limit=60

@celery.task
def add(x, y):
    return x + y


@celery.task
def run(req_id):

    # get data from database
    req = ExecutionRequest.query.get(req_id)

    lang = req.lang
    src = req.src

    f_name = str(uuid.uuid4().hex)
    f_ext = lang

    source = f'{f_name}.{f_ext}'

    with open(source, mode='w', encoding='utf-8') as f:
        f.write(src)

    #source = '<file>'

    if lang == 'py':
        result = py_runner(source)
    if lang == 'js':
        result = js_runner(source)
    if lang == 'c':
        result = c_runner(source)
    if lang == 'cpp':
        result = cpp_runner(source)

    returncode = result.returncode
    stdout = result.stdout
    stderr = result.stderr
    
    print(returncode)
    print(stdout)
    print(stderr)

    # update req with results
    req.is_completed = True
    req.returncode = returncode
    req.stdout = stdout
    req.stderr = stderr
    req.request_completed = datetime.utcnow()

    result = {
        "returncode": returncode,
        "stdout": stdout,
        "stderr": stderr
    }

    return result
