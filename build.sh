#!/usr/bin/env bash

set -o errexit

<<<<<<< HEAD
python manage.py collectstatic --noinput
=======
python manage.py collectstatic --noinput --verbosity 2
>>>>>>> main
python manage.py migrate
