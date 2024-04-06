FROM python:3.12.2-alpine3.19

WORKDIR /myapp

COPY requirements.txt /myapp/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /myapp
