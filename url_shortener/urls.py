"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from url_api.views import UrlViewSet
from rest_framework import routers
from shortener.views import MainView, RedirectView


routers = routers.DefaultRouter()
routers.register('', UrlViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shorten/api/', include(routers.urls)),
    path('', MainView.as_view()),
    path('<str:shorturl>/', RedirectView.as_view()),
]
