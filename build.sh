#!/usr/bin/env bash

set -o errexit

static/cup_of_english/images/about.jpg

python manage.py collectstatic --noinput
python manage.py migrate
