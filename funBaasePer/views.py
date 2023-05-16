from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response

from .models import *
from .serializers import StudentSerializer

from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def get_student(request):
    if request.method == 'GET':
        obj=Student.objects.all()
        serializer=StudentSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(StudentSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
