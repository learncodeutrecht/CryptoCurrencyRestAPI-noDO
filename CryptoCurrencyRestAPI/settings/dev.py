from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c*6j$t$rvmqhbq1v=rwvm*1_u(lmf7ew%e#+xa=oq8@9*p1wtb'

ALLOWED_HOSTS = ['188.166.66.158', ]

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crypto_currency_compare',
        'USER': 'crypto_compare_admin',
        'PASSWORD': 'jD44%!KP$',
        'HOST': '188.166.66.158',
        'PORT': '5432',
    }
}

CORS_ORIGIN_ALLOW_ALL=True

#CORS_ORIGIN_WHITELIST = (
#)
