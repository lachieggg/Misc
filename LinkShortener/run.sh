#!/bin/bash

# Migrations
python3 djangoapp/manage.py makemigrations
python3 djangoapp/manage.py migrate
# Environment
source .env
source .venv/djangodev/bin/activate
# Install dependencies
pip install -r requirements.txt
python3 djangoapp/manage.py runserver 0:8000