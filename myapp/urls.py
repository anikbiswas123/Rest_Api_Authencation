
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('app.urls')),
    # path('',include('RelApp.urls')),
    # path('',include('sessionapp.urls')),
    # path('',include('customPer.urls')),
    path('',include('funBaasePer.urls')),
]
