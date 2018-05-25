

from django.conf.urls import url
from . import views;

app_name = 'company'

urlpatterns = [
    url(r'^$' , views.CompanyListView.as_view() , name="all-company"),
    url(r'^profile-settings/$' , views.ProfileSettingsView.as_view() , name="profile-settings")
]
