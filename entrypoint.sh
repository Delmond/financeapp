#!/bin/sh



# Commit any migrations if available
python ./manage.py makemigrations
python ./manage.py migrate
#
## Start the celery worker service which executes tasks
celery -A financeapp worker -l info &
### Start the celery beat service which distributes tasks across workers
celery -A financeapp beat -l info & # --scheduler django_celery_beat.schedulers:DatabaseScheduler &

# Start the django server
python ./manage.py runserver 0.0.0.0:8000

