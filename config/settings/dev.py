from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_TOOLBAR_PANELS = [
'debug_toolbar.panels.versions.VersionsPanel',
'debug_toolbar.panels.timer.TimerPanel',
'debug_toolbar.panels.settings.SettingsPanel',
'debug_toolbar.panels.headers.HeadersPanel',
'debug_toolbar.panels.request.RequestPanel',
'debug_toolbar.panels.sql.SQLPanel',
'debug_toolbar.panels.staticfiles.StaticFilesPanel',
'debug_toolbar.panels.templates.TemplatesPanel',
'debug_toolbar.panels.cache.CachePanel',
'debug_toolbar.panels.signals.SignalsPanel',
'debug_toolbar.panels.logging.LoggingPanel',
'debug_toolbar.panels.redirects.RedirectsPanel',
]

# Application definition

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]


# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ALLOWED_HOSTS = ["aup.ci", "localhost"]

INTERNAL_IPS=['127.0.0.1']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'aupci_DB',
#         'USER': 'postgres',
#         'PASSWORD': 'Ferdi',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# EAMIL SETTINGS

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="mail.aup.ci"
EMAIL_HOST_USER="contact@aup.ci"
EMAIL_HOST_PASSWORD="Amour1>Uranus1>Pied"
EMAIL_PORT=587  #587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False

