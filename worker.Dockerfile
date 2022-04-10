# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# add maintainer

# add linux user 

#WORKDIR /app

# set enviroment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc g++

ENV NODE_VERSION=16.13.0
RUN apt install -y curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
RUN node --version
RUN npm --version

RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install greenlet
RUN pip install gunicorn
RUN pip install supervisor

COPY . /app

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD [ "gunicorn", "--bind=0.0.0.0:5000", "app:app" ]