#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate --noinput

# Start Gunicorn server
gunicorn django_pro.wsgi:application --bind 0.0.0.0:$PORT
