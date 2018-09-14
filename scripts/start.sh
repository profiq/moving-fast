#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate

daphne -b 0.0.0.0 -p 5000 config.asgi:application
