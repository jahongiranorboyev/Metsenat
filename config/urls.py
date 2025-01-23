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

from django.contrib import admin
from django.urls import path, include
from apps.authentication.views import send_verification_code, login

urlpatterns = [
    path('admin/', admin.site.urls),

    # users app
    path('api/v1/users/', include('apps.users.urls')),

    # Student-Sponsors app
    path('api/v1/studentsponsors/', include('apps.sponsors.urls')),

    # Universities app
    path('api/v1/general/', include('apps.general.urls')),

    # Appeals app
    path('api/v1/appeals/', include('apps.appeals.urls')),

    path('auth/send-code/', send_verification_code, name='send_verification_code'),  # Verification code yuborish
    path('auth/login/', login, name='login'),
]

