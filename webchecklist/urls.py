from django.contrib import admin
from django.urls import path, include

from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('adminsecurexxx/', admin.site.urls),
    
    path('', include('secureapp.urls')),
    
    path('', include(tf_urls)),
]
