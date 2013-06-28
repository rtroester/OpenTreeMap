#See
# http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango
# https://docs.djangoproject.com/en/1.3/howto/deployment/modwsgi/
#RT 3/18/13 change opentreemap to OpenTreeMap to make incorrect 1.2 & jlivni code happy
#RT 6/4/13 change name of this file from otm to mtm and 'OpenTreeMap' to mtm
#after dealing with remaining incorrect old treemap/management/commands code
#remove even mtm prefix where possible

import os, sys

# Redirect stdout to stderr to avoid annoying crashes
sys.stdout = sys.stderr

sys.path.append('/var/www/mtm')
sys.path.append('/var/www')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
main_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.insert(0, main_path)

import settings
import site

if hasattr(settings,"VENV_PATH") and settings.VENV_PATH:
    sys.path.insert(1, settings.VENV_PATH)

import django.core.management
django.core.management.setup_environ(settings)
utility = django.core.management.ManagementUtility()
command = utility.fetch_command('runserver')

command.validate()

import django.conf
import django.utils

django.utils.translation.activate(django.conf.settings.LANGUAGE_CODE)

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

