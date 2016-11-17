"""
Django settings for shopelectro project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from datetime import datetime
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# It is fake-url. Correct url will be created on `docker-compose up` stage from `docker/.env`
SECRET_KEY = os.environ.get('SECRET_KEY', 'so_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# http://bit.ly/sorl-thumbnail-docs
THUMBNAIL_DEBUG = False

# setting from docker example: https://github.com/satyrius/paid/
ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',')]

# https://docs.djangoproject.com/en/1.9/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Enable in frame loading for Ya.Metric
# https://docs.djangoproject.com/es/1.10/ref/clickjacking/
# https://yandex.ru/support/metrika/general/counter-webvisor.xml#download-page
X_FRAME_OPTIONS = 'ALLOWALL'

# Application definition
INSTALLED_APPS = [
    # https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#django.contrib.admin.autodiscover
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'mptt',
    'widget_tweaks',
    'sorl.thumbnail',
    'generic_admin',
    'images',
    'pages',
    'catalog',
    'ecommerce',
    'shopelectro',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'shopelectro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ecommerce.context_processors.cart',
                'shopelectro.context_processors.shop'
            ],
        },
    },
]

WSGI_APPLICATION = 'shopelectro.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LOCALE_NAME = 'en_US'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

FORMAT_MODULE_PATH = [
    'shopelectro.formats',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'front/build'),
    ASSETS_DIR,
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# It is fake-url. Correct url will be created on `docker-compose up` stage from `docker/.env`
DATABASE_URL = 'postgres://user:pass@db_name/table'
DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        default=DATABASE_URL
    )
}

PRODUCTS_TO_LOAD = 30

SITE_CREATED = datetime(2013, 1, 1)

LOCALHOST = 'http://127.0.0.1:8000/'
BASE_URL = 'https://www.shopelectro.ru'

PLACEHOLDER_IMAGE = 'images/common/logo.svg'
PLACEHOLDER_ALT = 'Логотип компании Shopelectro'

# Autocomplete and search settings
SEARCH_SEE_ALL_LABEL = 'Смотреть все результаты'

# For sitemaps and sites framework
SITE_ID = 1
SITE_DOMAIN_NAME = 'www.shopelectro.ru'


# Used to retrieve instances in ecommerce.Cart
CART_ID = 'cart'

# Used to define choices attr in definition of Order.payment_type field
PAYMENT_OPTIONS = (
    ('cash', 'Наличные'),
    ('cashless', 'Безналичные и денежные переводы'),
    ('AC', 'Банковская карта'),
    ('PC', 'Яндекс.Деньги'),
    ('GP', 'Связной (терминал)'),
    ('AB', 'Альфа-Клик'),
)

# It is fake-pass. Correct pass will be created on `docker-compose up` stage from `docker/.env`
YANDEX_SHOP_PASS = os.environ.get('YANDEX_SHOP_PASS', 'so_secret_pass')

# Used for order's email in ecommerce app
FAKE_ORDER_NUMBER = 6000

# Subjects for different types of emails sent from SE.
EMAIL_SUBJECTS = {
    'call': 'Обратный звонок',
    'order': 'Заказ №{0.fake_order_number}',
    'yandex_order': 'Заказ №{0.fake_order_number} | Яндекс.Касса',
    'one_click': 'Заказ в один клик №{0.fake_order_number}',
    'ya_feedback_request': 'Оцените нас на Яндекс.Маркете',
}

# Email configs
# It is fake-pass. Correct pass will be created on `docker-compose up` stage from `docker/.env`
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'so_secret_pass')
EMAIL_HOST_USER = 'info@shopelectro.ru'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'info@shopelectro.ru'
DEFAULT_TO_EMAIL = 'info@shopelectro.ru'
SHOP_EMAIL = 'info@shopelectro.ru'

# Used in admin image uploads
MODEL_TYPES = {
    'Product': {
        'app_name': 'shopelectro',
        'dir_name': 'products',
    },
    'Category': {
        'app_name': 'shopelectro',
        'dir_name': 'categories',
    }
}

# This need for using {% debug %} variable in templates.
INTERNAL_IPS = (
    '127.0.0.1',
)

TOP_PRODUCTS = [291, 438, 1137, 2166, 2725, 2838, 3288, 3642, 3884, 3959]

SHOP = {
    'id': '69886',
    'scid': '64788',
    'success_url': BASE_URL + '/shop/order-success/',
    'fail_url': BASE_URL + '/',
    'cps_phone': '+78124163200',
    'cps_email': 'info@shopelectro.ru',
    'local_delivery_cost': 300,
    'local_delivery_cost_threshold': 3000,
}

# used in data-migrations and tests
CUSTOM_PAGES = [{
    'slug': '',
    '_title': 'Интернет-магазин Элементов питания с доставкой по России',
    'h1': 'Интернет-магазин элементов питания "ShopElectro"',
    '_menu_title': 'Главная',
}, {
    'slug': 'order',
    '_title': 'Корзина Интернет-магазин shopelectro.ru Санкт-Петербург',
    'h1': 'Оформление заказа',
}, {
    'slug': 'search',
    '_title': 'Результаты поиска',
}, {
    'slug': 'catalog',
    '_title': 'Каталог товаров',
    'h1': 'Каталог товаров',
    '_menu_title': 'Каталог',
}, {
    'slug': 'order-success',
    '_title': 'Заказ принят',
    'h1': 'Заказ принят',
}]
