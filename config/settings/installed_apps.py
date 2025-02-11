DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.users',
    'apps.appeals',
    'apps.sponsors',
    'apps.general',
    'apps.permissions',
    'apps.authentication',
]
THIRD_PARTY_APPS =[
    'drf_yasg',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',


]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS