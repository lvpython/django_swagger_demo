from apps.settings.base import *
import os

#This option for fabric
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY",'a')
