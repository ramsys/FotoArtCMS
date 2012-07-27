from settings import *


DEBUG = False
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqlite3.db'),
    }
}


SECRET_KEY = 'your-super-secret-key'


MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', '/media/')


from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())

