import os, sys
site_user_root_dir = '/home/d/darbulat/dokizhingi.ru/public_html'
sys.path.insert(0, site_user_root_dir + '/HelloDjango')
sys.path.insert(1, '/home/d/darbulat/.local/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloDjango.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
