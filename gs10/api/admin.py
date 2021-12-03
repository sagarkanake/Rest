# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Student 
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'roll', 'city']