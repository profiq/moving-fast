# Moving Fast! demo chat application

**Author:** Filip Vavera

## Application

TODO: describe application

## Run locally

  * Install [Docker](https://docs.docker.com/install/#supported-platforms) and
    [docker-compose](https://docs.docker.com/compose/install/).
  * Create your application settings `cp example.env .env` (you can leave
    everything default)
  * Download latest images `docker-compose pull`
  * Build the application Docker image `docker-compose build --pull`
  * Run the application `docker-compose up`
    * If you encounter bug that Postgres DB takes longer to start so Django
      fails to connect to it in separate terminal run `docker-compose exec
      django python manage.py runserver 0.0.0.0:8000`
    * You can fix the bug by editting `scripts/start-dev.sh` file where you
      wait until the DB is reachable and starting the Django after that
  * Initialize your database `docker-compose exec django python manage.py
    migrate`
  * Create superuser account `docker-compose exec django python manage.py
    createsuperuser`
  * Enjoy application running on `http://localhost:8000` (you can login with
    your newly created account into administration at
    `http://localhost:8000/admin/`)

## Prepare development environment

  * Install
    [`pipenv`](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
  * Create your new Python environment `pipenv install`
  * Run the application as described in [Run locally](#run-locally) section
  * Edit code in your favourite Python editor (Vim is the only correct answer)

## Running tests

  * Prepare your environment as described in [previous
    section](#prepare-development-environment)
  * Run tests `pipenv run pytest`

## Deployment

TODO: describe deployment here
