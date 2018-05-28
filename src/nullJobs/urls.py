
from django.contrib import admin
from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static
from . import views;



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^apply/(?P<pk>\d+)/$' , views.ApplyView.as_view() , name="apply"),
    url(r'^accounts/' ,  include('accounts.urls'  , namespace="accounts" )),
    url(r'^company/' ,  include('company.urls'  , namespace="company" )),
    url(r'^employee/' ,  include('employee.urls'  , namespace="employee" )),
    url(r'^jobs/' ,  include('jobApplications.urls'  , namespace="jobApplications")),
    url(r'^tinymce/', include('tinymce.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
