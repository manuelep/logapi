import os
from pathlib import Path
from py4web.core import required_folder

USER_HOME = Path.home()

PY4WEB_APPS_FOLDER_NAME = os.getenv('PY4WEB_APPS_FOLDER_NAME') or 'py4web-apps'

APPS_PARENT = USER_HOME / PY4WEB_APPS_FOLDER_NAME 

APPS_FOLDER = Path(required_folder(APPS_PARENT / 'apps'))

APP_NAME = Path(__file__).parent.name

APP_FOLDER = APPS_FOLDER / APP_NAME
