import json
from py4web import action, request
from .common import logger

@action("index", method=['GET','POST'])
def index():
    logger.info(json.dumps(request.json, indent=4))
    return "Hello World"
