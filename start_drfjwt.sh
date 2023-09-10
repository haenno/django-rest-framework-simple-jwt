#!/bin/bash

echo 'drfjwt startup...'
python3 manage.py migrate --fake myapp
python3 manage.py makemigrations
python3 manage.py migrate --fake myapp
python3 manage.py makemigrations news
python3 manage.py makemigrations tasks
python3 manage.py migrate --fake myapp
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate news
python3 manage.py migrate
python3 manage.py migrate --fake myapp
python3 manage.py migrate --run-syncdb
python3 manage.py schemamigration news --auto
python3 manage.py schemamigration news --init
python3 manage.py migrate news
python3 manage.py migrate --run-syncdb    # Apply database migrations
python3 manage.py collectstatic --noinput # Collect static files
python3 manage.py loaddata db-seed.json
python3 manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
echo 'Starting drfjwt in production mode (Daphne):'
exec daphne -b 0.0.0.0 -p 8765 drfjwt.asgi:application
