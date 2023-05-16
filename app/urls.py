

from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import *


router=DefaultRouter()
# router.register('student',StudentModelViewset,basename='student')
# router.register('student1',StudentModelViewset1,basename='student1')


urlpatterns = [
    # path('',include(router.urls)),
    # path('',include(router.urls)),
    
]
