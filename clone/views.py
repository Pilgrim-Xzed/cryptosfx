from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect
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
   

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/dashboard')
        else:
            messages.error(request,'Check back in 24hrs')
            return redirect('login')

    else:
        form = AuthenticationForm()
    return render(request, 'password-reset/login.html', {'form': form})



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
