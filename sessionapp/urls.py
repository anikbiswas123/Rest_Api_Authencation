from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()

router.register('student',studentMOdelViewset,basename='student')


urlpatterns = [
    
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]
