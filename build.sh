#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations (uncomment the line below if you want to run migrations on each deployment)
# python manage.py migrate
