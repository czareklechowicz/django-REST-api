from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer
from .models import Cars
from .serializers import CarsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class CarsViewSet(viewsets.ModelViewSet):
    serializer_class = CarsSerializer

    def get_queryset(self):
        cars_warehouse = Cars.objects.all()
        return cars_warehouse
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = CarsSerializer(queryset, many=True)
        return Response(serializer.data)