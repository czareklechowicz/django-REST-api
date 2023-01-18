from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer
from .models import Cars
from .serializers import CarsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer