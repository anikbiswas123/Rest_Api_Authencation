from django.shortcuts import render
from  rest_framework import status

from .serializers import *
from .models import *

from rest_framework import viewsets

# Create your views here.
class AuthorModelViewset(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    

class BookMOdelViewset(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer    
    
