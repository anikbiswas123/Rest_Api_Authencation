from django.urls import path,include

from  .views import *

urlpatterns = [
    path('student_list/',get_student,name='student_list'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]
