# same base container as the frontend to save traffic and space 
FROM python:3.11.5-slim-bookworm
WORKDIR /srv/drfjwt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_USERNAME
RUN chmod +x start_drfjwt.sh
CMD ["sh", "start_drfjwt.sh"]
