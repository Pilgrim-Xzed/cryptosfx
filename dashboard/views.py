
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
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


class DepositView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/deposit.html'


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


class Support(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'dashboard/support.html'