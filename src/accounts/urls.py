

from django.conf.urls import url
from . import views;
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    url(r'^login/$' , views.LoginView.as_view() , name="login"),
    url(r'^register/$' , views.RegisterView.as_view() , name="register"),
    url(r'^logout/$' , views.LogoutView.as_view() , name="logout"),
    url(r'^account_activation_sent/$', views.AccountActivationView.as_view(), name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    #
    # url(r'^password-reset/$' , auth_views.password_reset ,{
    # 'template_name': 'registration/password_reset_form.html',
    # 'email_template_name': 'registration/password_reset_subject.txt',
    # 'html_email_template_name': 'registration/password_reset_email.html',
    # 'subject_template_name': 'registration/password_reset_subject.txt'
    # }, name="password-reset"),
    #
    # url(r'^password_reset/done/$', auth_views.password_reset_done,{'template_name': 'registration/password_reset_form.html'}, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'},name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete,{'template_name': 'registration/password_reset_done.html'}, name='password_reset_complete')
]
