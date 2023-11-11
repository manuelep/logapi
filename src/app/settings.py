"""
This is an optional file that defined app level settings such as:
- database settings
- session settings
- i18n settings
This file is provided as an example:
"""

import os, sys
from pathlib import Path
from py4web.core import required_folder

from logapi import settings

APP_NAME = settings.APP_NAME

STUFF_FOLDER = Path(required_folder(settings.APPS_PARENT / 'stuff' / APP_NAME))

(STUFF_FOLDER / '__init__.py').touch(exist_ok=True)

# USER_HOME = Path.home()

# APPS_FOLDER = USER_HOME / 'apps'

# APP_FOLDER = os.path.dirname(__file__)
# APP_NAME = os.path.split(APP_FOLDER)[-1]

# logger settings
LOGGERS = [
    "warning:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

sys.path.insert(0, str(STUFF_FOLDER))

# try import private settings
from settings_private import *
try:
    from settings_private import *
except (ImportError, ModuleNotFoundError):
    pass
