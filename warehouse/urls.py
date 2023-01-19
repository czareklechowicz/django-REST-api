
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from api import urls
import sys
sys.path.insert(1, '/Users/czareklechowicz/cars_warehouse/api/urls.py')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]
