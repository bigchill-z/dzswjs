from rest_framework import serializers
from .models import *


class RanksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Douyin
        fields = '__all__'
