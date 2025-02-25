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
    'apps.main_statistics',

]
THIRD_PARTY_APPS =[
    'drf_yasg',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',


]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
