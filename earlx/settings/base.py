import os

import dj_database_url

from .defaults import *


def boolify(s):
	m = {
		"0": False,
		"1": True,
	}
	return m[s]


def intify(s):
	return int(s)

DEBUG = os.getenv("DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")
SITE_ID = os.getenv("SITE_ID")

DATABASES = {'default': dj_database_url.config()}

INSTALLED_APPS += [
	"django.contrib.sites",
	"django.contrib.flatpages",
	"django.contrib.redirects",
]

# Note that the order of MIDDLEWARE_CLASSES matters.
# Generally, you can put RedirectFallbackMiddleware at the end of the list, because it’s a last resort.
MIDDLEWARE_CLASSES += [
	"django.contrib.redirects.middleware.RedirectFallbackMiddleware",
]

TEMPLATES[0]["DIRS"] += [
	os.path.join(BASE_DIR, 'templates'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir, "staticfiles"))
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
