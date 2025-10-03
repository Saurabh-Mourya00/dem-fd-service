#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

# Start Gunicorn server
gunicorn django_pro.wsgi:application --bind 0.0.0.0:$PORT
