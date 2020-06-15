from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
# Create your views here.
class Index(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'index.html'
