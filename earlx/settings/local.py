from .production import *

DEBUG = boolify(os.getenv("DEBUG", str(1)))
SECRET_KEY = os.getenv("SECRET_KEY")
SITE_ID = int(os.getenv("SITE_ID", str(1)))

ALLOWED_HOSTS = [
	"*",
]

INSTALLED_APPS += [
	"debug_toolbar",
]
