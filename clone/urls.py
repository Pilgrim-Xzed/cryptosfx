from django.urls import path, include
from .views import Index, about, trade, education, legal
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from users import urls as core_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/',include(core_urls), name='dashboard'),
    path('about/', about, name="about"),
    path('trade_center/', trade, name="trade"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password-reset/password_reset.html', subject_template_name='password-reset/password_reset_subject.txt', email_template_name='password-reset/password_reset_email.html',),
         name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    url(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                                template_name='password-reset/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset/password_reset_done.html'), name='password_reset_done'),

    path('', Index.as_view(), name="home"),
    path('education/', education, name="education"),
    path('legal/', legal, name="legal"),




]
