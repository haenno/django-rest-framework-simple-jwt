# same base container as the frontend to save traffic and space 
FROM node:18-bullseye
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install pipenv -y
WORKDIR /usr/src/drf_jwt_test
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY . .
RUN chmod +x start_drf_jwt_test.sh
CMD ["sh", "start_drf_jwt_test.sh"]
