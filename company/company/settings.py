"""
Django settings for company project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '312g0!2j4k8s&1i15+jk80hq*ktw3)mly4&j%i(uft&52_(x5q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*",]


# Application definition

INSTALLED_APPS = [
    'channels',
    'ckeditor',  
    'ckeditor_uploader',
    'introduce.apps.IntroduceConfig',
    'newuser.apps.NewuserConfig',
    'forum.apps.ForumConfig',
    'chat.apps.ChatConfig',
    'others.apps.OthersConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
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

ROOT_URLCONF = 'company.urls'

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

WSGI_APPLICATION = 'company.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'company',
        'USER': 'root',
        'PASSWORD': 'xxxxxxxx',
        'PORT': '3306',
        'HOST':'127.0.0.1',
        'charset':'utf8',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#user
AUTH_USER_MODEL = 'newuser.NewUser'

#ckeditor
CKEDITOR_UPLOAD_PATH = "ckeditor"
CKEDITOR_CONFIGS = {
    'default': {
        'width':1200,
        'toolbar': (
            ['Undo','Redo'],
            ['Save','Preview','Maximize','ShowBlocks',], 
            ['Styles','Format','Font','FontSize'], 
            ['Cut','Copy','Paste',], 
            ['SelectAll','RemoveFormat'], 
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
            ['Link','Unlink','Anchor'], 
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
            ['TextColor','BGColor',],
            ['Bold','Italic','Underline','Strike'], 
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','-','Subscript','Superscript'], 
        ),
    },
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}

#SESSION_COOKIE_AGE = 6 * 60 * 60 
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True 

LOGIN_URL = '/newuser/login/'

# Channels
ASGI_APPLICATION = 'company.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

#支付宝sdk
ALIPAY_APPID = "2088102176217764"
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"

#messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

#email------------------------------------------
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = 'han-xiansheng@qq.com' # 帐号
EMAIL_HOST_PASSWORD = 'xxx'  # 授权码，非邮箱登录密码，配置请百度。
DEFAULT_FROM_EMAIL = 'FDD<han-xiansheng@qq.com>'
