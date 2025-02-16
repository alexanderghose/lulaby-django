#Ensures the app runs in Python 3.10 inside Docker.
FROM python:3.10

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
# Installs all dependencies in an isolated environment.
RUN pip install pipenv && pipenv install --system

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
