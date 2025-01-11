import os
from django.conf import settings
from pathlib import Path
import dj_database_url
from datetime import timedelta
from dotenv import load_dotenv

import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    "corsheaders",
    'rest_framework',
    'rest_framework_swagger',
    'coreapi',
    'drf_yasg',
    'social_django',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework.authtoken',
    'django_rest_passwordreset',
    
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOWED_ORIGINS = [
    
# ]
CORS_ALLOW_ALL_ORIGINS = True
# CSRF_TRUSTED_ORIGINS = [

# ]

AUTHENTICATION_BACKENDS = [
    'account.backends.CustomAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'smartstudy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'UPLOADED_FILES_USE_URL': True,
}

WSGI_APPLICATION = 'smartstudy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if 'DATABASE_URL' in os.environ:
    database_url = os.environ.get("DATABASE_URL")
    DATABASES["default"] = dj_database_url.parse(database_url)
else:
    pass

# Cloudinary configuration
cloudinary.config(
    cloud_name = os.environ.get("CLOUD_NAME"),
    api_key = os.environ.get("CLOUD_API_KEY"),
    api_secret = os.environ.get("CLOUD_API_SECRET")
)

PAYSTACK_SECRET_KEY = os.environ.get("PAYSTACK_SECRET_KEY")
PAYSTACK_BASE_URL = os.environ.get("PAYSTACK_BASE_URL")

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

AUTH_USER_MODEL = 'account.User'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST'] # SMTP server
EMAIL_PORT = os.environ['EMAIL_PORT']  # Port for the SMTP server
EMAIL_USE_TLS = True  # Use TLS for secure communication
EMAIL_USE_SSL = False  # Use SSL (only one of TLS or SSL can be True)

EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']  # Your Zoho email address
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # Your Zoho email password or app-specific password
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']  # Display name and Zoho email address

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'