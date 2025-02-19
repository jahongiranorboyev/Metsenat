"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .drf_yasg import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users app
    path('api/v1/users/', include('apps.users.urls')),

    # Student-Sponsors app
    path('api/v1/student-sponsors/', include('apps.sponsors.urls')),

    # Universities app
    path('api/v1/general/', include('apps.general.urls')),

    # Appeals app
    path('api/v1/appeals/', include('apps.appeals.urls')),
    path('api/v1/permissions/', include('apps.permissions.urls')),

    # AUTH apps
    path('api/v1/auth/', include('apps.authentication.urls')),

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

