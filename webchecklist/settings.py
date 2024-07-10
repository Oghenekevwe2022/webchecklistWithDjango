
from pathlib import Path

# Django environ

import environ

env = environ.Env()

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('THE_SECRET_KEY')

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
    'secureapp',
    
    'crispy_forms',
    'crispy_bootstrap5',
    'django_recaptcha',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_email',
    'two_factor',
    'axes'
]

# Specify the template pack that is allowed

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Recaptcha keys

RECAPTCHA_PUBLIC_KEY = '6LfKJ-0pAAAAAOiH4DQhOHTcu1-ebUAcHScCMHqy'
RECAPTCHA_PRIVATE_KEY = '6LfKJ-0pAAAAAHzQCXjJ-FwZ8mdqMmmLxgWNsifc'

# 2FA

LOGIN_URL = 'two_factor:login'
LOGIN_REDIRECT_URL = 'dashboard'

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list
    'axes.backends.AxesStandaloneBackend',
    
    #Django ModelBackend is the default authentication backend
    'django.contrib.auth.backends.ModelBackend',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',   # 2FA
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'django_auto_logout.middleware.auto_logout', # Auto Logout
    
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list
    'axes.middleware.AxesMiddleware', # Axes
]

ROOT_URLCONF = 'webchecklist.urls'

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
                
                'django_auto_logout.context_processors.auto_logout_client', # Auto Logout
            ],
        },
    },
]

WSGI_APPLICATION = 'webchecklist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Edmonton'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static' ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auto Logout

from datetime import timedelta

AUTO_LOGOUT = {
    'IDLE_TIME': 15,   # Time in seconds i.e 15 seconds in this case
    
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    
    'MESSAGE': 'The session has expired. Please login again to continue'
}

# Axes configuration for brute attack (allows the number of failed login before blocking further logins)

AXES_FAILURE_LIMIT: 3 # Number of times a user can fail a login

AXES_COOLOFF_TIME: 2 # Wait 2 hours before attempting a login again

AXES_RESET_ON_SUCCESS = True # Reset failed login attempts

AXES_LOCKOUT_TEMPLATE = 'account-locked.html' # Add a custom template, page to display after unsuccessful login

AXES_LOCKOUT_PARAMETERS = ['username']   # Prevent brute force attacks by username, meaning other username will be allowed


# SMTP configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = 'True'

EMAIL_HOST_USER = 'elijahudi@gmail.com'   # Gmail email address
EMAIL_HOST_PASSWORD = 'gfim fbtv yxlf ssck'  # -APP password

DEFAULT_FROM_EMAIL = 'elijahudi@gmail.com'  # - Gmail email address

# Pre=deployment security options

# CSRF protection
"""
SESSION_COOKIE_SECURE = True
CSRF_COOKIES_SECURE = True

# SSL redirect

SECURE_SSL_REDIRECT = True

# Enable HSTS

SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
"""
# Look into a CSP (Content Security Policy)