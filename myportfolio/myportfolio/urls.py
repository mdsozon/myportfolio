"""myportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from . import settings as pro_settings

if pro_settings.DEBUG == False:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('machinebdapp.urls')),
        url('^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        url('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('portfolio.urls')),
    ]