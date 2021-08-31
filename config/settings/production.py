from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "wwww.aup.ci", "aup.ci", "45.86.162.6"]

# Application definition


#CRISPY_TEMPLATE_PACK = 'bootstrap4'

# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS=['www.aup.ci']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'aupci_DB',
#         'USER': 'postgres',
#         'PASSWORD': 'aupci2021',
#         'HOST': 'www.aup.ci',
#         'PORT': '5432',
#     }
# } 
