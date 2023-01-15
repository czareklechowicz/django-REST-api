
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from api import urls

urlpatterns = [
    path('api/', include(urls)),
    path('admin/', admin.site.urls)
]
