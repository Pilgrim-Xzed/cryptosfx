from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import ProfileView
urlpatterns = [
   path('', ProfileView.as_view(), name='profile'),
]
