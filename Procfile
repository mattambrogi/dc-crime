web: gunicorn django_project.wsgi --log-file -
worker: celery -A django_project.celery worker -B --loglevel=info