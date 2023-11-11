import os
from pathlib import Path
from . import settings

here = Path(__file__)

def link_logapi(app_name:str = settings.APP_FOLDER):
    os.symlink(here.parent.parent.absolute() / 'app', settings.APP_FOLDER)