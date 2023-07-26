"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import logging
from pathlib import Path

import django.utils.log
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aed)8z9%%!xlanu%mw4c-vlxbqbk&t!5ixfp=m&mezgs5y^q)!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    "django_apscheduler",
   # 'django_filters'

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    

]
# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',



            ],
        },
    },
]

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
LOGIN_REDIRECT_URL = "/news"

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

SITE_URL = 'http://127.0.0.1:8000'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
#EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://192.168.59.101:30548'
CELERY_RESULT_BACKEND = 'redis://192.168.59.101:30548'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['console_news_debug', 'console_news_warning', 'console_news_errors', 'general_news'],
            'level': 'DEBUG',
        },

        'django.request': {
            'handlers': ['mail_admins', 'errors_news'],
            'level': 'ERROR',
        },

        'django.server': {
            'handlers': ['mail_admins', 'errors_news'],
            'level': 'ERROR',
        },

        'django.template': {
            'handlers': ['errors_news'],
            'level': 'ERROR',
        },

        'django.db.backends': {
            'handlers': ['errors_news'],
            'level': 'ERROR',
        },

        'django.security': {
            'handlers': ['security_news'],
            'level': 'DEBUG',
        },
    },

    'handlers': {
        'console_news_debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'format_console_debug',
            'filters': ['require_true'],
        },
        'console_news_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'format_console_warning',
            'filters': ['require_true'],
        },
        'console_news_errors': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'format_console_errors',
            'filters': ['require_true'],
        },

        'general_news': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'format_general',
            'filters': ['require_false'],
        },

        'errors_news': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'format_errors',
        },

        'security_news': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'format_security',
        },

        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'format_mail',
            'filters': ['require_false'],
        },
    },

    'filters': {
        'require_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'formatters': {
        'format_console_debug': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'stile': '{',
        },
        'format_console_warning': {
            'format': '%(asctime)s - %(levelname)s - %(message)s -  %(pathname)s',
            'stile': '{',
        },
        'format_console_errors': {
            'format': '%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(exc_info)s',
            'stile': '{',
        },

        'format_general': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s',
            'stile': '{',
        },
        'format_errors': {
            'format': '%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(exc_info)s',
            'stile': '{',
        },
        'format_security': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s',
            'stile': '{',
        },
        'format_mail': {
            'format': '%(asctime)s - %(levelname)s - %(message)s - %(pathname)s',
            'stile': '{',
        },
    },
}