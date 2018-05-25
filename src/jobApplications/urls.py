

from django.conf.urls import url
from . import views;

app_name = 'jobApplications'

urlpatterns = [
    url(r'^post/$' , views.JobPostingView.as_view() , name="job-post"),
    url(r'^previous-posts/$' , views.PreviousPostingsView.as_view() , name="previous-post"),
    url(r'^previous-posts/update/(?P<pk>\d+)/$' , views.PreviousPostingsUpdateView.as_view() , name="job-post-update"),
    url(r'^previous-posts/delete/(?P<pk>\d+)/$' , views.PreviousPostingsDeleteView.as_view() , name="job-post-delete"),
]
