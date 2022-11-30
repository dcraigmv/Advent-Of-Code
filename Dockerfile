FROM python:3.9 AS build

ENV PYTHONPATH /app

COPY . /app
WORKDIR /app

CMD python -u day1/part1.py