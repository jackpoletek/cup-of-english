#!/usr/bin/env bash

set -o errexit

python manage.py collectstatic --noinput --verbosity 2
python manage.py migrate
