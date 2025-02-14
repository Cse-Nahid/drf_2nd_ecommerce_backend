
from pathlib import Path
import os
import environ
env = environ.Env()
environ.Env.read_env()



# Build paths inside the project like this: BASE_DIR / '
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sr7y-s0n7ibjf^-#jll&p!g)=31%p*751y_&+p7)#@1=(@bb+$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ "127.0.0.1",
    ".vercel.app",
    "https://drf-2nd-ecommerce-backend.vercel.app/",
    ]




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "whitenoise.runserver_nostatic",
    'corsheaders',
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',  # For token-based authentication
    'dj_rest_auth',  # For user authentication
    'allauth',  # Required for registration
    'allauth.account',  # Required for registration
    'dj_rest_auth.registration',  # For registration
    'allauth.socialaccount',
    'django_filters',

    # my apps
    'users',  
    'products',
    'categories',
    'dashboard',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "corsheaders.middleware.CorsMiddleware",
    'allauth.account.middleware.AccountMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", 
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates",],
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

WSGI_APPLICATION = 'ecommerce.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.cujzpiuqnbnnukwujnje',
        'PASSWORD': 'EWcDIctVvcvDo2xV',
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com', 
        'PORT': '6543'
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT= BASE_DIR / "staticfiles"
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # Token-based authentication
        'rest_framework.authentication.SessionAuthentication',  # Default session-based authentication
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  
    ],
    
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # Make sure this is included
    ],
}


SSLCOMMERZ = {
    'store_id': 'nahid67aeb2a98b6c6',
    'store_pass': 'nahid67aeb2a98b6c6@ssl',
    'sandbox': True  # Set to False in production
}
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "pk_test_51QsL8sFtvDPVochCerjA9iyWAs2gDYbEzANTuKRksKtopE2tUtHQDqJ0vHOOPSmxacIkFggF8meEpOQyZH8Vgyov009t0KMszw")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "sk_test_51QsL8sFtvDPVochCQLAQRtxP4SCqhY8oi2kXhf0W5zaEFhsLst9ZAzqQkW3dmlm7Ir8d0R6q1cgTevt3JBZTF63N00V43MPcDk")



CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:7000",
    "http://127.0.0.1:5500",  # Add this if not already present
    "https://ecommerce-api.onrender.com",
    "https://drf-2nd-ecommerce-backend.vercel.app",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5500",  # Add this if not already present
    "https://ecommerce-api.onrender.com",
    "https://drf-2nd-ecommerce-backend.vercel.app"
]

CORS_ALLOW_CREDENTIALS = True



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'