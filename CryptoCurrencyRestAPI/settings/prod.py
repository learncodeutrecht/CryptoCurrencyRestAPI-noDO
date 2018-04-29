from .base import *

import json

from django.core.exceptions import ImproperlyConfigured

with open('/srv/greenery_marketplace/backend/greenery_marketplace_backend/settings/secrets.json') as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """
    Get the secret variable or return explicit exception.
    """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

#ALLOWED_HOSTS = ['136.144.191.109', ]
ALLOWED_HOSTS = ['*']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': get_secret('DJANGO_DB_ENGINE'),
        'NAME': get_secret('DJANGO_DB_NAME'),
        'USER': get_secret('DJANGO_DB_USER'),
        'PASSWORD': get_secret('DJANGO_DB_PASSWORD'),
        'HOST': get_secret('DJANGO_DB_HOST'),
        'PORT': get_secret('DJANGO_DB_PORT'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     '136.144.191.109',
# )