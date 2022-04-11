from . import *

SECRET_KEY = os.environ.get("SECRET_KEY", SECRET_KEY)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blankxx',
        'USER': 'blankxx',
        'PASSWORD': 'enurox123',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
