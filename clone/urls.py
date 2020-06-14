from django.urls import path
from .views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),

    
   
   
]