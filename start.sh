#!/bin/bash
flask db upgrade
gunicorn manage:app --bind=0.0.0.0:5000