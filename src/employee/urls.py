

from django.conf.urls import url
from . import views;

app_name = 'employee'

urlpatterns = [
    url(r'^details/$' , views.ProfileSettingsView.as_view() , name="details"),
    url(r'^education-details/$' ,  views.EmployeeEducationDetailsView.as_view() , name="education-details"),
    url(r'^professional-details/$' ,  views.EmployeeProfessionalDetailsView.as_view() , name="professional-details"),
    url(r'^resume/$' ,  views.EmployeeResumeDetailsView.as_view() , name="resume"),
    url(r'^profile/(?P<slug>[\w-]+)/$' , views.EmployeeProfileView.as_view() , name="profile")
]
