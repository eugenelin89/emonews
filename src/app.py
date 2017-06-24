# app.py

from __future__ import print_function
from flask import Flask, request, make_response, abort, logging
import urllib, json, os, sys, requests, tasks
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
    #tasks.add.delay(1,2)
    return "Good Test!"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)