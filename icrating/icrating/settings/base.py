# settings/base.py
# At the top of settings/base.py
from unipath import Path
PROJECT_ROOT = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_ROOT.child('media')
STATIC_ROOT = PROJECT_ROOT.child('static')
STATICFILES_DIRS = (
    PROJECT_ROOT.child('assets')
)
TEMPLATE_DIRS = (
    PROJECT_ROOT.child('templates')
)

import os
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured
def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Then, in any of your settings $les, you can load secret keys from environment variables as follows:

# SOME_SECRET_KEY = get_env_variable("SOME_SECRET_KEY")
