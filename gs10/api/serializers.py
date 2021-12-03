from .models import Student
from rest_framework import serializers


# Create your views here.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll' , 'city']