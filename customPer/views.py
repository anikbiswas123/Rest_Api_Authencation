from django.shortcuts import render,redirect
from rest_framework import status

from rest_framework import viewsets
from .models import *
from .serializers import *
from .CustomPermission import *



# Create your views here.
class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    permission_classes=[Mypermission]
