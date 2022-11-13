#!/bin/bash

pip install -r requirements.txt

python3 app.py

tail -f /dev/null
