import os
from pathlib import Path
from configurations import Configuration
from configurations import values
import dj_database_url


class Dev(Configuration):
	# Build paths inside the project like this: BASE_DIR / 'subdir'.
	BASE_DIR = Path(__file__).resolve().parent.parent

	# Quick-start development settings - unsuitable for production
	# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

	# SECURITY WARNING: keep the secret key used in production secret!
	SECRET_KEY = 'django-insecure-pnq1_%ee9t9na!)1br)eb9ray+wf_!+py5=0@e3zexydbq_v86'

	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = values.BooleanValue(True)

	ALLOWED_HOSTS = ["*"]

	# X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
	# CSRF_COOKIE_SAMESITE = None
	# CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
	# CSRF_COOKIE_SECURE = True
	# SESSION_COOKIE_SECURE = True
	# CSRF_COOKIE_SAMESITE = 'None'
	# SESSION_COOKIE_SAMESITE = 'None'

	# Application definition

	INSTALLED_APPS = [
		"django.contrib.sites",
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'blog',

		'crispy_forms',
		'crispy_bootstrap5',
		'debug_toolbar',
		'blango_auth',
		'django_registration',
		'rest_framework',
		'rest_framework.authtoken',

		'allauth',
		'allauth.account',
		'allauth.socialaccount',
		'allauth.socialaccount.providers.google',
	]

	SITE_ID = 1

	ACCOUNT_USER_MODEL_USERNAME_FIELD = None
	ACCOUNT_EMAIL_REQUIRED = True
	ACCOUNT_USERNAME_REQUIRED = False
	ACCOUNT_AUTHENTICATION_METHOD = "email"

	CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

	CRISPY_TEMPLATE_PACK = "bootstrap5"

	INTERNAL_IPS = ["192.168.11.179"]

	AUTH_USER_MODEL = "blango_auth.User"

	EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

	ACCOUNT_ACTIVATION_DAYS = 7

	MIDDLEWARE = [
		"debug_toolbar.middleware.DebugToolbarMiddleware",
		'django.middleware.security.SecurityMiddleware',
		'django.contrib.sessions.middleware.SessionMiddleware',
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.contrib.auth.middleware.AuthenticationMiddleware',
		'django.contrib.messages.middleware.MessageMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
		'allauth.account.middleware.AccountMiddleware',
	]

	ROOT_URLCONF = 'BlangoPro.urls'

	TEMPLATES = [
		{
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [BASE_DIR / 'templates']
			,
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

	WSGI_APPLICATION = 'BlangoPro.wsgi.application'

	# Database
	# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': BASE_DIR / 'db.sqlite3',
		}
	}
	# DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")

	# Password validation
	# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

	PASSWORD_HASHERS = [
		'django.contrib.auth.hashers.Argon2PasswordHasher',
		'django.contrib.auth.hashers.PBKDF2PasswordHasher',
		'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
		'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
	]

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
	# https://docs.djangoproject.com/en/5.1/topics/i18n/

	LANGUAGE_CODE = 'en-us'

	# TIME_ZONE = 'UTC'
	TIME_ZONE = values.Value("UTC")

	USE_I18N = True

	USE_L10N = True

	USE_TZ = True

	# Static files (CSS, JavaScript, Images)
	# https://docs.djangoproject.com/en/5.1/howto/static-files/

	STATIC_URL = '/static/'

	# Default primary key field type
	# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

	DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

	ADMINS = [("Ben Shaw", "ben@example.com"), ("Leo Lucio", "leo@example.com")]
	DJANGO_ADMINS = "Ben Shaw,ben@example.com;Leo Lucio,leo@example.com"

	LOGGING = {
		"version": 1,
		"disable_existing_loggers": False,
		"filters": {
			"require_debug_false": {
				"()": "django.utils.log.RequireDebugFalse",
			},
		},
		"formatters": {
			"verbose": {
				"format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
				"style": "{",
			},
		},
		"handlers": {
			"console": {
				"class": "logging.StreamHandler",
				"stream": "ext://sys.stdout",
				"formatter": "verbose",
			},
			"mail_admins": {
				"level": "ERROR",
				"class": "django.utils.log.AdminEmailHandler",
				"filters": ["require_debug_false"],
			},
		},
		"loggers": {
			"django.request": {
				"handlers": ["mail_admins"],
				"level": "ERROR",
				"propagate": True,
			},
		},
		"root": {
			"handlers": ["console"],
			"level": "DEBUG",
		}
	}

	REST_FRAMEWORK = {
		"DEFAULT_AUTHENTICATION_CLASSES": [
			"rest_framework.authentication.BasicAuthentication",
			"rest_framework.authentication.SessionAuthentication",
			"rest_framework.authentication.TokenAuthentication",
		]
	}


class Prod(Dev):
	DEBUG = False
	SECRET_KEY = values.SecretValue()
