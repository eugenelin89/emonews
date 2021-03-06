# https://www.cloudamqp.com/docs/celery.html
import celery, os, requests, json, random
from analysis import analyze_article



app = celery.Celery('demo')
app.conf.update(
    BROKER_URL=os.environ['CLOUDAMQP_URL'],
    BROKER_POOL_LIMIT=20,
    BROKER_HEARTBEAT = None,
    CELERY_RESULT_BACKEND = os.environ['REDIS_URL'],
    CELERY_SEND_EVENTS = False,
    CELERY_EVENT_QUEUE_EXPIRES = 60)

@app.task
def add(a, b):
    ''' test '''
    return {'result' : a + b}

@app.task
def analyze(url):
    result = analyze_article(url)
    result["prediction"] = random.randint(0, 1) # Intent is to use actual result when bug is fixed.
    return result #analyze_article(url) #{'url':url}
