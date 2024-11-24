#!/bin/bash
python manage.py migrate

python manage.py collectstatic

# gunicorn --workers 2 hackathon.wsgi
python manage.py runserver 0.0.0.0:8000