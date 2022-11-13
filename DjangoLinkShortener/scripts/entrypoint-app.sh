#!/bin/bash

source .venv/bin/activate

# Install dependencies
python3 -m pip install -r requirements.txt
# Run migrations
python3 djangoapp/manage.py makemigrations
python3 djangoapp/manage.py migrate
# Copy database
cp djangoapp/db.sqlite3.orig djangoapp/db.sqlite3
# Allow read/write permissions
chown -R $USER djangoapp/db.sqlite3
chmod a+r djangoapp/db.sqlite3
source .env
# Run server
python3 djangoapp/manage.py runserver 0:8000
tail -f /dev/null
