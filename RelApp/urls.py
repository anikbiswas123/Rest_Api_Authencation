from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import *

router=DefaultRouter()

# router.register('Author',AuthorModelViewset,basename='Author')
# router.register('Book',BookMOdelViewset,basename='Book')

urlpatterns = [
    
    # path('',include(router.urls)),
    # path('',include(router.urls))
    
]
