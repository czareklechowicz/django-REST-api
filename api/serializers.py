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
        fields = ['brand', 'model', 'year', 'kilometers', 'horse_power', 'description']