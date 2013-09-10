import os, sys

base = os.path.dirname(os.path.dirname(__file__))
base_parent = os.path.dirname(base)

sys.path.append(base)
sys.path.append(base_parent)

os.environ['DJANGO_SETTINGS_MODULE'] = 'diary.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
