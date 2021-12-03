# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.response import Response


# Create your views here.

# When is send GET request to this app then this method get automatically called and it send the response
# @api_view()
# def hello_world(request):
#     return Response({'msg', 'hello world'})

# but you can also mention GET  here
# @api_view(['GET',])
# def hello_world(request):
#     return Response({'msg', 'hello world'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#       print(request.data)  
#       return Response({'msg', 'hello world'})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg' : 'This is GET Request '})
    if request.method == 'POST':
      print(request.data)
      return Response({'msg' : 'hello world', 'data' : request.data})