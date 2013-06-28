# RT 11/28/12 from https://github.com/jlivni/OpenTreeMap/blob/master/settings_philadelphia.py
# RT 3/10/13 other additions from sandiego, etc
# RT 3/24/13 add settings from 1.3 local_settings_examples.py
#
import os

from choices import *

# RT 3/24/13 was in settings_sandiego.py - believe early form so comment out
#GOOGLE_API_KEY = 'abcdf'

API_KEY_GOOGLE_MAP = ''
# RT 3/24/13 1.3 has 2 values, 1 commented out
API_KEY_GOOGLE_ANALYTICS = "IGNORE"
#API_KEY_GOOGLE_ANALYTICS = 'UA-23175691-1'


GEOSERVER_URL = 'http://mtm.weuns.lan:8080/geoserver/wms?transparent=true'
#RT 5/8/13 use search view in geo layer, constant tree map in tilecache layer
GEOSERVER_GEO_LAYER = 'otm:tree_search'
GEOSERVER_GEO_STYLE = ''

#RT 5/6-23/13 try running tilecache under wsgi from /var/www/tilecache
#accessing from our virtual host mtm.weuns.lan - NOT localhost
#old: TILECACHE_URL = 'http://localhost/cgi-bin/tilecache.cgi/'
#only works ON local system: TILECACHE_URL = 'http://localhost/tilecache/'
TILECACHE_URL = 'http://mtm.weuns.lan/tilecache/'

#RT 6/27/13 need elucidation on new polygons
#thought it would be for neighborhoods separate from trees
#seems to be for woodland polygons but still needs to be defined
#as something or otm crashes
#TILECACHE_LAYER = 'treemap_plot'

TILECACHE_LAYER = 'treemap'
TILECACHE_POLYGON_LAYER = 'treemap_neighborhood'


#RT 3/20/13 used in templates/Montpelier/template_4.html (same as above?):
TC_URL = 'http://mtm.weuns.lan/tilecache/'
#TC_URL = 'http://localhost/cgi-bin/tilecache.cgi/'

# RT 3/24/13 as used in 1.3 also from sandiego
COMPLETE_ARRAY = ['species','condition','sidewalk_damage','powerline_conflict_potential','canopy_height','canopy_condition','dbh','width','length','type']
#another jlivni city example uses a shorter array
#COMPLETE_ARRAY = ['species','condition','sidewalk_damage','powerline_conflict_potential','dbh','plot_width','plot_length','plot_type']

#django.contrib.staticfiles wants STATIC_ROOT, STATIC_URL, and
#STATICFILES_DIRS, _STORAGE, and _FINDERS
STATIC_URL = '/static/'
# RT 3/24/13 1.3 uses STATIC_ROOT = '/usr/local/otm/static' without trailing /
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/')
# RT 3/24/13 1.3 for running collectstatic(?)
#STATICFILES_DIRS = (
#    '/usr/local/otm/app/static',
#)

SITE = 'Montpelier'
#RT 3/7/13 verify! much (jlivni) code assumes '/' site root
#RT 3/18/13 give in and change /otm to /
SITE_ROOT='/'

SITE_LOCATION = 'Montpelier'
PENDING_ON = False
REGION_NAME = 'Montpelier'

MAP_CLICK_RADIUS = .0015 # in decimal degrees

LOGIN_REDIRECT_URL = '/'

ADMINS = (
    ('admin', 'jb@weuns.lan'),
)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL= 'jb@weuns.lan'
CONTACT_EMAILS = ['jb@weuns.lan']
EMAIL_MANAGERS = False

TILED_SEARCH_RESPONSE = False

# separate instance of tilecache for dynamic selection tiles
CACHE_SEARCH_TILES = True
CACHE_SEARCH_METHOD = 'disk' #'disk'
CACHE_SEARCH_DISK_PATH = os.path.join(os.path.dirname(__file__), 'local_tiles/')
CACHE_BACKEND = 'file:///tmp/trees_cache'
MAPNIK_STYLESHEET = os.path.join(os.path.dirname(__file__), 'mapserver/stylesheet.xml')

#RT 5/13/13 test debug values
#DEBUG = False

# sorl thumbnail settings
THUMBNAIL_DEBUG = False
THUMBNAIL_SUBDIR = '_thumbs'
#2/3/13 remove #
THUMBNAIL_EXTENSION = 'png'
#THUMBNAIL_QUALITY = 95 # if not using png

# django-registration
REGISTRATION_OPEN = True # defaults to True
ACCOUNT_ACTIVATION_DAYS = 5

EMAIL_USE_TLS = True # gmail used True
EMAIL_HOST = 'mx.weuns.lan'
EMAIL_HOST_USER = 'jb'
EMAIL_HOST_PASSWORD = 'friend'
EMAIL_PORT = 25 # gmail used 587

DATABASES = {
    'default': {
        'NAME': 'otmdb',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'postgres', # Not used with sqlite3.
        'PASSWORD': 'postgres', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

#RT 5/13/13 currently 'example.com. is site 1, 'localhost' is site 2 !!!
#used by flatpages app only (well, sites app, too)
#RT 5/30/13 changed example.com to weuns.lan (now site 1) and removed localhost,
#then couldn't log in! so change site_id to match! more than just flatpages!
SITE_ID = 1

# RT 2/11/13, 3/7/13 ?
# RT 3/18/13 give in and change /otm to /
# RT 3/24/13 uses ROOT_URL = ""
ROOT_URL = "http://mtm.weuns.lan/"

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# RT 3/24/13 1.3 uses weird '..'
# RT 4/15/13 change back - papa knows best or does he
#MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '..', 'media/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# 2/11/13, 3/7/13 ?
# RT 3/18/13 give in and change /otm to /
#MEDIA_URL = 'http://localhost/media/'

# RT 3/24/13 2 versions from 1.3 with and without initial slash
#4/29/13 test
#MEDIA_URL = 'media/'
#4/20/13 test
#MEDIA_URL = '' doesnt work

# RT 5/5/13 per django staticfiles doc if using static.serve as is done in urls.py
#must have initial slash
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# RT 3/24/13 1.3 uses weird '..'
# RT 4/15/13 again, trust papa or do we
#ADMIN_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '..', 'admin_media/')
# RT 3/26/13 collectstatic put admin media in static/admin, so ...
# not sure of ADMIN_MEDIA_PREFIX???
ADMIN_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static/admin/')
ADMIN_MEDIA_PREFIX = '/admin_media/'

# RT 3/24/13 1.3 uses weird '..'
# RT 4/15/13 papa again, NOT
#STATIC_DATA = os.path.join(os.path.dirname(__file__), '..', 'static/')
STATIC_DATA = os.path.join(os.path.dirname(__file__), 'static/')

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'insecure'

# RT 3/24/13 1.3 followed main 'templates' with /usr/local/app/templates
# but templates are used in order of listing - want overrides first
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates/Montpelier'),
    os.path.join(os.path.dirname(__file__), 'templates'),
)

#-------------------
#RT 3/24/13 below from 1.3 not in original settings_sandiego.py

FORCE_SCRIPT_NAME = ''

# RT 3/24/13 modify 1.3 version which was for Great Britain Treezilla`
# 3/29/13 use City Hall as center
BOUNDING_BOX = { # WKID 4326
    'left': -72.6053869,
    'bottom': 44.2303371,
    'right': -72.5453869,
    'top': 44.2903371
}

MAP_CENTER_LAT = 44.2603371
MAP_CENTER_LON = -72.5753869

REPUTATION_SCORES = {
    'add tree': 25,
    'add plot': 25,
    'edit tree': 5,
    'edit plot': 5,
    'add stewardship': 5,
    'remove stewardship': -5,
    'edit verified': {
        'up': 5,
        'down': -10,
        'neutral': 1,
    },
}

EXTRAPOLATE_WITH_AVERAGE = True

# pipeline minification settings
# RT 3/26/13 easy-install put yuicompressor (not yiu-compressor)
# in /usr/local/bin
PIPELINE = False
PIPELINE_ROOT = os.path.dirname(__file__)
PIPELINE_URL = '/'
PIPELINE_YUI_BINARY = '/usr/local/bin/yuicompressor'
PIPELINE_YUI_JS_ARGUMENTS = '--nomunge'
PIPELINE_JS = {
    'base': {
        'source_filenames': (
            SITE_ROOT + 'static/js/jquery_mods.js',
            SITE_ROOT + 'static/treemap.js',
            SITE_ROOT + 'static/js/utils.js',
            SITE_ROOT + 'static/js/map.js',
            SITE_ROOT + 'static/js/map_init.js',
            SITE_ROOT + 'static/js/geocode.js',
            SITE_ROOT + 'static/js/page_init.js',
            SITE_ROOT + 'static/js/management.js',
            SITE_ROOT + 'static/js/comments.js',
        ),
        'output_filename': 'static/all_base.js',
    },
    'map': {
        'source_filenames': (
            SITE_ROOT + 'static/js/map.js',
            SITE_ROOT + 'static/js/threaded.js',
         ),
        'output_filename': 'static/all_map.js',
    }
}

# RT 3/24/13 1.3 better version than one I had from 12.04 install instructions
# 11/29/12 added "just to start" - but text had error: MAPS instead of MAP
# required keys are addsame, add, edit and view. Values and order can change.
# Edit tree_add view to change/add allowed keys
ADD_FORM_TARGETS = [
    ('addsame', 'I want to add another tree using the same tree details'),
    ('add', 'I want to add another tree with new details'),
    ('edit','Let me continue editing this tree'),
    ('view', 'I\'m done!'),
]

ADD_FORM_TARGETS_DEFAULT = 'view'

#RT 5/30/13 TEST!
#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/tmp/mtm-mail'
