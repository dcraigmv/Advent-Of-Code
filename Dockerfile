FROM python:3.9 AS build

ENV PYTHONPATH /app

COPY . /app
WORKDIR /app

CMD sh -c 'for d in day*; do echo "\n$d"; python -u $d/part1.py; python -u $d/part2.py; done'