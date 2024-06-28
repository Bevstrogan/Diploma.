import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-vpvsd0%a*6n1s4@w+wmt*$loc_p4zw^pw6z@e8e21iwii%m3&5"

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_celery_beat',
    "rest_framework",
    "djoser",
    "users",
    "ads",
    "redoc",
    "drf_yasg",
    "corsheaders"
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "skymarket.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "skymarket.wsgi.application"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication', ]
    ,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
}


DJOSER = {
    'SERIALIZERS': {
        'user_create': 'users.serializers.UserRegistrationSerializer'
    },
    'LOGIN_FIELD': 'email'
}


DATABASES = {
    "default": {
        "ENGINE": os.getenv('DB_ENGINE'),
        "NAME": os.getenv('DB_NAME'),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


AUTH_USER_MODEL = "users.User"

STATIC_URL = "/django_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "django_static")

MEDIA_URL = "/django_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "django_media")


CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]

CORS_ALLOW_ALL_ORIGINS = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")


