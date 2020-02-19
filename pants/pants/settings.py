"""
Django settings for pants project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decimal import Decimal

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["PANTS_DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'ingredients.apps.IngredientsConfig',
    'products.apps.ProductsConfig',
    'recipes.apps.RecipesConfig',
    'diary.apps.DiaryConfig',
    'targets.apps.TargetsConfig',
    'website.apps.WebsiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pants.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),],
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

WSGI_APPLICATION = 'pants.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'
#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Added settings below here....

LOGIN_URL = '/wearpants/'

# Constants used for nutritional calculations
# DO NOT EDIT THESE
# They are chemical constants, not preferences
KJ_PER_KCAL = Decimal(4.184)
G_PER_KG = Decimal(0.001)
KJ_PER_G_CARB = Decimal(16.7) # 16.7kj energy per gram of carbs/protein
KJ_PER_G_PROT = Decimal(16.7)
KJ_PER_G_FAT = Decimal(37.7)
#KJ_PER_G_ALC = Decimal(29.3)   # Alcohol. not used yet
# Source for above is the National Health and Medical Research Council, Australia.

# User settings below here.....

# Ratio of protein used for synthesis vs used for energy.
# This varies with the amount of excess protein in the diet and
# exercise but we are assuming 75% for the moment (FIXME: add refs here)
# This MUST be between 0 and 1.
# Affects "Rank" calculation
PROT_SYNTH_FACTOR = Decimal(0.6)

# Assorted Constants used in various models
NAME_LENGTH = 100
SLUG_LENGTH = 50
TAG_LENGTH = 20      # Also used for column length for some data
DESCR_LENGTH = 250

# XXX DO NOT EDIT THIS - TODO some code still assumes KG
STANDARD_WEIGHT = 1000 # All values stored in KG = 1000g

# FIXME KLUDGE - we should be able to do without these, nutrition data
# should be managed by a class
# XXX important
# These are the minimum dict keys in nutrition data returned from
# recipe and ingredient cached property nutrition_data
# This allows us to treat them interchangeably in many places and
# cache the relevant data for recipe components etc.
NUTRITION_DATA_ITEMS = ('protein','fibre','kilojoules','carbohydrate','fat','sugar','grams','cost')
# Note cost and grams on the end, used for per-X calculations
# Ingredient grams is constant for all ingredients - see STANDARD_WEIGHT

# Without grams and cost
NUTRITION_DATA_ITEMS_BASIC = ('protein','fibre','kilojoules','carbohydrate','fat','sugar')

# With all items and ratios calculated - this is the most data that
# will be returned apart from sub-object data (amino acids, vitamins etc)
NUTRITION_DATA_ITEMS_EXTENDED = ('protein','fibre','kilojoules','carbohydrate','fat','sugar','grams','cost','protein_per_cost','fibre_per_cost','protein_per_j','fibre_per_j','pf_per_j','rank')

# Decimal Quantization settings - this controls the significant
# figures shown to users and used in some calculations
#DECIMAL_PLACES = Decimal('0.001')
#DECIMAL_PLACES_KCAL = Decimal('0.01')
#DECIMAL_PLACES_KJ = Decimal('0.1')
DECIMAL_PLACES = Decimal('0.01')
DECIMAL_PLACES_KCAL = Decimal('0.1')
DECIMAL_PLACES_KJ = Decimal('1')
DECIMAL_CENTS = Decimal('0.01')

