web: newrelic-admin run-program gunicorn config.wsgi --log-file -
celeryworker: celery worker --app=config.celery_app.app --loglevel=INFO --without-gossip --without-mingle --without-heartbeat --max-tasks-per-child 1000
celerybeat: celery beat --app=config.celery_app.app --loglevel=INFO
