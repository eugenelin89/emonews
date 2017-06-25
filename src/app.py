# app.py

from __future__ import print_function
from flask import Flask, request, make_response, abort, logging
import urllib, json, os, sys, requests, tasks
from celery.result import AsyncResult
# _access_token and _post_msg_url will eventually be moved to another module/process for sending messages.

#########
# Setup #
#########
app = Flask(__name__)
# We put _menu here because it stays in memory and reduce fetching from firebase.
_menu = None

#########
# Flask #
#########

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    abort(401)

@app.route("/test", methods=['GET'])
def test():
    res = tasks.add.delay(1,2) # test
    return res.id

@app.route("/result", methods=['GET'])
def get_result():
    id = request.args.get('id')
    res = AsyncResult(id)
    data = {'ready':res.ready()}
    if data['ready']:
        print('Ready')
        data['result'] = res.get(timeout = 1)
        print(data)
    return str(data)

@app.route("/news")
def get_analysis():
    url = request.args.get('url')
    return url



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
