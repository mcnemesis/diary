import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
BASE_URL = '/diary/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG


#customize...
ADMINS = (
    ('Nemesis Fixx', 'joewillrich@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Could switch to 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'magic_diary',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

#customize...
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Kampala'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '%s/media/' % PROJECT_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '%s/media/' % BASE_URL

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '%s/static/' % PROJECT_ROOT

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '%s/static/' % BASE_URL

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o+1!u+er^q!kmoyzy@*%arvj$q7ig%1aq$@=gj*v4j7m_z3t&t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'diary.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'diary.wsgi.application'

TEMPLATE_DIRS = (
    '%s/templates/' % PROJECT_ROOT,
) + tuple([ '%s/%s/templates/' % (PROJECT_ROOT, c) for c in ['magic']]) #app-specific templates

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.markup',
    'django_admin_bootstrapped',

    'django.contrib.admin',
    'magic',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


TEMPLATE_CONTEXT_PROCESSORS  = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "diary.context_processors.customisation",
)


#Magical Diary Settings: Please customize
APP_NAME = "Magical Diary"
MAGICIAN_NAME = "Nemesis Fixx"
HOME_TITLE = "The Nemesis Diary"
SITE_DESCRIPTION = "The magical diary of Nemesis Fixx"
#The Site's About information is configured here (supports using MarkDown)
MAGICIAN_ABOUT = '''

A little background
-------------------

Am Nemesis Fixx (also known as Lutalo Joseph Willrich), a Ugandan by birth, and a machine programmer by proffession.

Occult Interests
----------------

I have been actively interested in phenomena of the LHP since 2006, and before that was an active member of the +RCC, before I decided to quit.

Since around 2009, my interests in the Occult diversified into other many other paths and dimensions, and of late, my will is to advance myself and the craft in a modern, pragmatic and systematic manner. Currently, my major influences are probably from the schools of Chaos Magic and Modern Satanism.

Other Interests
---------------

I've tried to live a full and balanced life (in the short time during this incarnation). I write software, make music, write poetry, create art, ride my bike, meet friends, make love and practice magic.

Contact
-------

Should you need to contact me, you might catch me any of the following dimensions:

    - Google+ (Joe Willrich Lutalo)
    - GitHub (mcnemesis)
    - GMail (joewillrich)
    - IRC (nemesisfixx : freenode)
    - LinkedIn (Joe Willrich Lutalo)
    - SoundCloud (Nemesis Fixx)
    - LastFM (Nemesis Fixx)
    - DeviantArt (nemesisfixx)

Philosophy
----------

    A life unexplored is not worth living
        - Socrates
'''


INSTALLED_THEMES = [
        {'name' : 'Slate', 'value' : 'slate'},
        {'name' : 'Cyborg', 'value' : 'cyborg'},
        {'name' : 'Cosmo', 'value' : 'cosmo'},
        ]

#----------- LOGGING ----------------
from errno import EEXIST
from dateutil.easter import datetime
import logging

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != EEXIST:
            raise

LOG_DIR = '%s/logs' % PROJECT_ROOT
make_sure_path_exists(LOG_DIR)
MAIN_LOG = '%s/log_%s' % (LOG_DIR,datetime.date.strftime(datetime.date.today(),'%b_%d_%Y'))
LOG_LEVEL = logging.ERROR
