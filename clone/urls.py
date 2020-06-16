from django.urls import path
from .views import Index, about, trade, education, legal
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('about/',about, name="about"),
    path('trade_center/',trade, name="trade"),
    path('education/',education, name="education"),
    path('legal/',legal, name="legal"),

    
   
   
]