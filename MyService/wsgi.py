"""
WSGI config for MyService project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyService.settings")
#
# application = get_wsgi_application()

import os
import sys

path = '/home/almond/Service'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Service.settings.production'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())