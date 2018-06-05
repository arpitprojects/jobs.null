

from django.conf.urls import url
from . import views;

app_name = 'jobApplications'

urlpatterns = [
    url(r'^$' , views.ExploreJobs.as_view() , name="job-post"),
    # url(r'^post-as-guest/$' , views.PostJobAsGuest.as_view() , name="job-post-guest"),
    url(r'^post/$' , views.JobPostingView.as_view() , name="job-post"),
    url(r'^previous-posts/$' , views.PreviousPostingsView.as_view() , name="previous-post"),
    url(r'^previous-posts/update/(?P<pk>\d+)/$' , views.PreviousPostingsUpdateView.as_view() , name="job-post-update"),
    url(r'^previous-posts/delete/(?P<pk>\d+)/$' , views.PreviousPostingsDeleteView.as_view() , name="job-post-delete"),
    url(r'^view-applications/(?P<pk>\d+)/$' , views.ViewApplicationView.as_view() , name="view-applications"),
    url(r'^view-applications/(?P<superkey>\d+)/update/(?P<pk>\d+)/$' , views.ViewApplicationUpdateView.as_view() , name="update-applications"),
    url(r'^view-applications/(?P<superkey>\d+)/delete/(?P<pk>\d+)/$' , views.ViewApplicationDeleteView.as_view() , name="delete-applications")
]
