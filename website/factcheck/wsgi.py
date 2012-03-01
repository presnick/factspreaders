import os
import django.core.handlers.wsgi
import sys

sys.path.append('/srv/factspreaders/production/website/')
sys.path.append('/srv/factspreaders/production/website/factcheck')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "factcheck.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
#from django.core.handlers.wsgi import get_wsgi_applica
#application = get_wsgi_application()
application = django.core.handlers.wsgi.WSGIHandler()
