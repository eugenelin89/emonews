web: gunicorn --pythonpath src app:app --log-file -
worker: celery worker --workdir src --app=tasks.app --without-gossip --without-mingle --without-heartbeat
