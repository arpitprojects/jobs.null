

from django.conf.urls import url
from . import views;

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$' , views.LoginView.as_view() , name="login"),
    url(r'^register/$' , views.RegisterView.as_view() , name="register"),
    url(r'^logout/$' , views.LogoutView.as_view() , name="logout"),
    url(r'^account_activation_sent/$', views.AccountActivationView.as_view(), name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate')
]
