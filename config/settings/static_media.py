# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
from django.conf import settings

STATIC_URL = 'static/'
STATIC_ROOT = settings.BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = settings.BASE_DIR / 'media'