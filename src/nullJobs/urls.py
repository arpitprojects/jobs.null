
from django.contrib import admin
from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static
from . import views;



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^about-us/$' , views.AboutView.as_view() , name="about"),
    url(r'^contact-us/$' , views.ContactView.as_view() , name="contact"),
    url(r'^terms/$' , views.TermsView.as_view() , name="terms"),
    url(r'^privacy/$' , views.PrivacyView.as_view() , name="privacy"),
    url(r'^press/$' , views.PressView.as_view() , name="press"),
    url(r'^faq/$' , views.FAQView.as_view() , name="faq"),
    url(r'^apply/(?P<pk>\d+)/$' , views.ApplyView.as_view() , name="apply"),
    url(r'^accounts/' ,  include('accounts.urls'  , namespace="accounts" )),
    url(r'^company/' ,  include('company.urls'  , namespace="company" )),
    url(r'^employee/' ,  include('employee.urls'  , namespace="employee" )),
    url(r'^jobs/' ,  include('jobApplications.urls'  , namespace="jobApplications")),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/get_job_title/', views.get_job_title, name='get_job_title'),
    url(r'^api/location/', views.location, name='location'),
] #location
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
