#!/usr/bin/env bash

set -o errexit

python manage.py findstatic cup_of_english/images/about.jpg --verbosity 2
python manage.py collectstatic --noinput
python manage.py migrate
