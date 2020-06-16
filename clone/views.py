from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
# Create your views here.
class Index(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'index.html'



def about(request):
    return render(request, 'about.html',{})


def trade(request):
    return render(request, 'forex.html',{})


def education(request):
    return render(request, 'education.html',{})



def legal(request):
    return render(request, 'legal.html',{})
