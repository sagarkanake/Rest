# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE', ])
def student_api(request):
    if request.method == 'GET':
       id =  request.data.get('id')
       if id is not None:
           stu = Student.objects.get(id = id)
           serializer = StudentSerializer(stu)
           return Response(serializer.data)
       stu = Student.objects.all()
       serializer = StudentSerializer(stu, many=True)
       return Response(serializer.data)
    if request.method == 'POST':
        json_data = request.data  
        serializer = StudentSerializer(data = json_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created' })    
        return Response(serializer.errors)    
    if request.method == 'PUT':
        json_data = request.data
        id = json_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = json_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg', 'Data Updated'})
        return Response(serializer.errors)
    if request.method == 'DELETE' :
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg' : 'Data deleted'})
    
             
        
        

