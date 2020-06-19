from django.urls import path, include
from .views import Index, about, trade, education, legal, Success, login, contactus,asset_index
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
    url(r'^login/$', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset/password_reset_done.html'), name='password_reset_done'),

    path('', Index.as_view(), name="home"),
    path('success/', Success.as_view(), name="success"),
    path('education/', education, name="education"),
    path('legal/', legal, name="legal"),
    path('contactus/', contactus, name="contact"),
    path('asset_index/', asset_index, name="asset"),




]
