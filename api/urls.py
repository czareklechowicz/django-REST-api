from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'cars', views.CarsViewSet, basename='Cars')


urlpatterns = [
    path('', include(router.urls)),
]