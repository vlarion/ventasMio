from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'rj7j^bw2jtvrv@(f^_b)7%w#-2)-il-45dsy-(yggq!mwus&#d'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mantenedor.apps.MantenedorConfig',    
    'bootstrap4',
    'crispy_forms'
]


CRISPY_TEMPLATES_PACK='bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ventas.urls'

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

WSGI_APPLICATION = 'ventas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
#   'default': {
#        'ENGINE': 'django.db.backends.oracle',
#        'NAME': 'www.harrys.cl/xe',
#        'USER': 'ICKA',
#        'PASSWORD': 'MACARENA',
    #    'HOST': 'localhost',
    #    'PORT': '1521',
 #   }
    
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
       'NAME': 'xe',
        'USER': 'ventas',
        'PASSWORD': 'amanoiaku',
#        'HOST': 'localhost',
#        'PORT': '1521',
    }
    
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.oracle',
#       'NAME': 'xe',
#        'USER': 'tecno',
#        'PASSWORD': 'tecno',
#        'HOST': 'localhost',
#        'PORT': '1521',
#    }
#    
#}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/index/'
LOGOUT_REDIRECT_URL = '/index/'
