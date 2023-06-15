from rest_framework import serializers
from .models import *
#from rest_framework.parsers import JSONParser


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ['title', 'descr', 'image', 'sort_descr']