
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import SignUpForm, ProfileForm

# Create your views here.


class DashboardView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/dashboard.html'


class ProfileView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/profile.html'


class InvestmentView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/invest.html'


class WithdrawView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/withdraw.html'


def deposit(request):
    model = User
    amount = request.GET.get('amount')
    return render(request, 'dashboard/deposit.html', {"amount": amount})


class EcalenderView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/calender.html'


class TsignalView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/dashboard.html'


class MkView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/market.html'


def support(request):
    if request.method == 'GET':
        print(request.GET.get('sub'))
        send_mail(
            request.GET.get('sub'),
            request.GET.get('message'),
            'helpbox@coinwintrade.com',
            ['helpbox@coinwintrade.com'],
            fail_silently=True,
        )
    else:
        form = {}
    return render(request, 'dashboard/support.html', {})
