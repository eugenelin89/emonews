# https://www.cloudamqp.com/docs/celery.html
import celery, os, requests, json



app = celery.Celery('demo')
app.conf.update(
    BROKER_URL=os.environ['CLOUDAMQP_URL'],
    BROKER_POOL_LIMIT=20,
    BROKER_HEARTBEAT = None,
    CELERY_RESULT_BACKEND = None,
    CELERY_SEND_EVENTS = False,
    CELERY_EVENT_QUEUE_EXPIRES = 60)

@app.task
def add(a, b):
    ''' test '''
    return a + b
