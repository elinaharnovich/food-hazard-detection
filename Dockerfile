FROM python:3.12-slim

WORKDIR /app

RUN pip install pipenv

COPY data/incidents_train.csv data/incidents_train.csv
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --ignore-pipfile --system

COPY food_hazard_detector .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app:app