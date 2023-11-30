FROM python:alpine3.18

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
