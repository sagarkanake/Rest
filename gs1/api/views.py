# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Model Object - Single Student Data
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    #print(stu)
    serializer = StudentSerializers(stu)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    
    #return HttpResponse(json_data, content_type= 'application/json')
              #OR
    return JsonResponse(serializer.data, safe = True, )

# Query - Set - All student data
def student_list(request):
    stu = Student.objects.all()
    #print(stu)
    serializer = StudentSerializers(stu, many=True)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
 
    #return HttpResponse(json_data, content_type= 'application/json')
            #OR
    return JsonResponse(serializer.data, safe = False)         
 
 
