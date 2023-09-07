#!/bin/bash

echo 'Django DRF startup...'
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate --run-syncdb  # Apply database migrations
pipenv run python manage.py collectstatic --noinput  # Collect static files
pipenv run python manage.py loaddata db-seed.json
export DJANGO_SUPERUSER_PASSWORD=admin
pipenv run python manage.py createsuperuser --username admin --email haenno@web.de --noinput
echo 'Starting Django in production mode (Daphne):'
exec pipenv run daphne -b 0.0.0.0 -p 8765 drfjwt.asgi:application
