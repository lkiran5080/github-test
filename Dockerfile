# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# add maintainer

# add linux user 

#WORKDIR /app

# set enviroment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install greenlet
RUN pip install gunicorn
RUN pip install supervisor

COPY . /app

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD [ "gunicorn", "--bind=0.0.0.0:5000", "app:app" ]