# django-rest-framework-simple-jwt

A Django REST framework and Simple JWT installation for testing with frontend projects.

Espacially for usage with my frontend project: <https://github.com/haenno/vue-tf>

My test installation is running at: <https://drfjwt.haenno.de>

## API endpoints for JWT authentication

- Obtain a token pair for a user: POST to ``/api/token/obtain/`` with ``username, password``
- Verify a token: POST to ``/api/token/verify/`` with ``token``  *(works on both access and refresh tokens)*
- Refresh a token: POST to ``/api/token/refresh/`` with ``refresh`` *(refresh token only, returns fresh access and refresh tokens)*
- Blacklist a token: POST to ``/api/token/blacklist/`` with ``refresh`` *(blacklists any kind of token, refresh or access)*

## Usage

Clone this repo to your local system, copy the ``example.env`` file to ``.env`` and adjust it to your needs. Then start the docker container with ``docker-compose up -d``.

The porject should also run without docker, even if there are some error messages while installung the packeges from the requirements.txt file (at least on my windows system). But it works.

If you like, fist create a virtual environment with conda:

```bash
conda create --name drfjwt python=3.11
conda activate drfjwt
```

Then prepare the project:

```bash
git clone *this repo*
pip install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations newsapi
python manage.py makemigrations tasks
python manage.py migrate
python manage.py loaddata db-seed.json
python manage.py createsuperuser
```

And finally start the server for local testing with ``python manage.py runserver``.

Then open <http://127.0.0.1:8000/> in your browser and login with the superuser credentials. Usefull for testing is also:

- The Djnago Admin interface: <http://127.0.0.1:8000/admin>
- Any mistyped URL, as it will show you the available URLs :-)

## Notes

- The default lifetime of the access token is 1 minute, the refresh token is 10 minutes.
