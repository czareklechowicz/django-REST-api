from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cars


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'brand', 'model', 'price', 'year', 'kilometers', 'horse_power', 'description', 'broken']

class CarsMiniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ['brand']