from rest_framework import serializers
from .models import Student

#Validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be start with r ')
     
class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators = [starts_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
    
    # Field level Validataion
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'ganesh' and ct.lower() != 'pune':
            raise serializers.ValidationError('City must be Pune   ')
        return data
        