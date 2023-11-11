import json
from py4web import action, request
from .common import logger

@action("index", method=['GET','POST'])
@action("log/<action>", method=['GET','POST'])
def index(action:str='index'):
    logger.info(f'Hook received to action {action} with payload: {json.dumps(request.json, indent=4)}')
    return "Hello World"
