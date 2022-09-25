from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Teacherinfo

class Studentserializer(serializers.Serializer):
    cid=serializers.IntegerField()
    name=serializers.CharField(max_length=70)
    email=serializers.EmailField(max_length=70)
    #password=serializers.CharField(max_length=70)
    #teacher_info=serializers.CharField(max_length=70)

    def create(self, validate_data):
        return Teacherinfo.objects.create(**validate_data)
