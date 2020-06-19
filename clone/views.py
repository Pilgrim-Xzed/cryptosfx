from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
# Create your views here.
class Index(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('success')
    template_name = 'index.html'
    popup = False

    
    def form_valid(self, form):
        form.send_email()
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        context["popup"] = self.popup
        return context
   



def about(request):
    return render(request, 'about.html',{})

class Success(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('success')
    template_name = 'index.html'
    popup = True

    def form_valid(self, form):
        form.send_email()
        self.popup = True
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        context["popup"] = self.popup
        return context


def trade(request):
    return render(request, 'forex.html',{})


def education(request):
    return render(request, 'education.html',{})



def legal(request):
    return render(request, 'legal.html',{})
