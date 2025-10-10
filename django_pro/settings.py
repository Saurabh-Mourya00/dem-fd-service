# import os
# from pathlib import Path
# from decouple import config
# import dj_database_url


# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY")

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []  # No restrictions for local development

# # Application definition

# INSTALLED_APPS = [
#     "blog.apps.BlogConfig",    # Blog->app->blogconfig see all html files 
#     "users.apps.UsersConfig",
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "crispy_forms",
#     "crispy_bootstrap4",
#     'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.google',
#     'storages',
# ]

# SOCIALACCOUNT_LOGIN_ON_GET = True

# SITE_ID = 1

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
#     "allauth.account.middleware.AccountMiddleware",
# ]

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# ROOT_URLCONF = "django_pro.urls"

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'OAUTH_PKCE_ENABLED': True,
#         'CLIENT_ID': config('GOOGLE_CLIENT_ID'),
#         'SECRET': config('GOOGLE_CLIENT_SECRET'),
#     }
# }

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WSGI_APPLICATION = "django_pro.wsgi.application"

# # Database
# # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# # Configure PostgreSQL for local development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DATABASE_NAME'),
#         'USER': config('DATABASE_USER'),
#         'PASSWORD': config('DATABASE_PASSWORD'),
#         'HOST': config('DATABASE_HOST'),
#         'PORT': config('DATABASE_PORT'),
#     }
# }

# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

# USE_I18N = True

# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
# CRISPY_TEMPLATE_PACK = 'bootstrap4'

# LOGIN_REDIRECT_URL = 'blog-home'
# LOGIN_URL = 'login'

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # Email settings
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config("E_PASS")  # Your SMTP email
# EMAIL_HOST_PASSWORD = config("G_PASS")  # Your SMTP password
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

import os
from pathlib import Path
from decouple import config
import dj_database_url
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=True)

# Allowed hosts
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")

# Application definition
INSTALLED_APPS = [
    "blog.apps.BlogConfig",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap4",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'storages',
]

SOCIALACCOUNT_LOGIN_ON_GET = True
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = "django_pro.urls"

LOGIN_REDIRECT_URL = 'blog-home'
LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
        'CLIENT_ID': config('GOOGLE_CLIENT_ID'),
        'SECRET': config('GOOGLE_CLIENT_SECRET'),
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_pro.wsgi.application"

# Static and media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # final collected location
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # where your source CSS/JS/images live

# Serve compressed static files via Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (if you use user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = config("E_PASS")
EMAIL_HOST_PASSWORD = config("G_PASS")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Database configuration
USE_SUPABASE = config("USE_SUPABASE", default=False, cast=bool)

if USE_SUPABASE:
    # Use Supabase for production/test
    DATABASES = {
        "default": dj_database_url.parse(config("SUPABASE_DB_URL"))
    }
else:
    # Local Postgres
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': config('DATABASE_HOST'),
            'PORT': config('DATABASE_PORT'),
        }
    }

import logging
logging.basicConfig(level=logging.INFO)


# if USE_SUPABASE:
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     # Use Supabase Storage S3-compatible API
#     # NOTE: Supabase S3 gateway uses dedicated S3 credentials, NOT the normal API keys.
#     # Keep previous lines for reference:
#     # AWS_ACCESS_KEY_ID = config('SUPABASE_KEY')
#     # AWS_SECRET_ACCESS_KEY = config('SUPABASE_SECRET')
#     AWS_ACCESS_KEY_ID = config('SUPABASE_S3_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = config('SUPABASE_S3_SECRET_ACCESS_KEY')
#     # Prefer bucket from env to avoid hard-coding
#     AWS_STORAGE_BUCKET_NAME = config('SUPABASE_BUCKET', default='profile')
#     # S3 endpoint and public object domain derived from SUPABASE_URL
#     _SUPABASE_URL = config('SUPABASE_URL')
#     # Path-style addressing is required for Supabase S3 API
#     AWS_S3_ADDRESSING_STYLE = 'path'
#     AWS_S3_ENDPOINT_URL = f"{_SUPABASE_URL}/storage/v1/s3"
#     # Generate public, unsigned URLs that match Supabase public bucket scheme
#     AWS_S3_CUSTOM_DOMAIN = f"{_SUPABASE_URL.replace('https://', '').replace('http://', '')}/storage/v1/object/public"
#     AWS_DEFAULT_ACL = 'public-read'
#     AWS_QUERYSTRING_AUTH = False
#     AWS_S3_FILE_OVERWRITE = False
#     # Ensure MEDIA_URL points to Supabase public object base
#     MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"


AWS_S3_REGION_NAME = 'ap-south-1'  # e.g. 'us-east-1'
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

# Optionally:
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Set media / default file storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
