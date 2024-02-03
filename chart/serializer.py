from rest_framework import serializers
from .models import *

class data_Serializer(serializers.ModelSerializer):
    class Meta:
        model=datas
        fields="__all__"
