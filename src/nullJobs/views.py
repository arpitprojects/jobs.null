from django.shortcuts import render ,HttpResponse , redirect , HttpResponseRedirect
from django.views.generic import CreateView , TemplateView , DetailView , UpdateView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from accounts.models import CommonUserProfile
from accounts.decoraters import employer_required , employee_required;
from django.utils.decorators import method_decorator
from itertools import chain
from jobApplications.models import JobPostingModel ,JobApply
from company.models import CompanyProfile
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import json
from .forms import ContactModelForm

def location(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = JobPostingModel.objects.filter(location__icontains=q).distinct()
    results = []

    for pl in places:
      place_json = {}
      place_json = pl.location
      results.append(place_json)

    results = list(set(results)); #inside for inside if
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def get_job_title(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = JobPostingModel.objects.filter(job_title__icontains=q).distinct()
    results = []
    for pl in places:
      place_json = {}
      place_json = pl.job_title
      results.append(place_json)

    results = list(set(results));
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

class HomeView(ListView):
    template_name = "home/index.html"
    queryset = JobPostingModel.objects.filter(is_active = True).order_by('-id')
    paginate_by = 5;
    count = 0;

    def get_context_data(self , *args, **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['count'] = self.count;
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request;
        query = request.GET.get("q" , None)

        if query is not None:
            filter_active = JobPostingModel.objects.filter(is_active = True)
            company_results = JobPostingModel.objects.search(query).filter(is_active = True)
            queryset_chain = chain(
                company_results
            )
            qs = sorted(queryset_chain , key = lambda instance : instance.pk , reverse = True)
            self.count= len(qs);
            return qs

        return JobPostingModel.objects.filter(is_active = True).order_by('-id')

@method_decorator([employee_required] , name="dispatch")
class ApplyView(SuccessMessageMixin , LoginRequiredMixin , View):
    # model = JobApply
    # fields = '__all__'pp
    # template_name = "jobposting/jobapply_form.html"
    def get(self , request , *args , **kwargs):
        val = self.request.user;

        employer = JobPostingModel.objects.get(pk = self.kwargs['pk']);


        # End of the email to the employee as well as employer
        jobapply = JobApply(employee = val ,job_app = (JobPostingModel.objects.get(pk = self.kwargs['pk'])))
        jobapply.save();

        #For employee
        subject_c = 'Your application for '+employer.job_title+' at '+employer.jobposting.name+" is submitted"

        from_e = settings.EMAIL_HOST_USER

        to_c = val.email

        message_c = render_to_string('employee_message.html', {
            'company_name': employer.jobposting.name,
            'job_title': employer.job_title,
        })
        

        c = send_mail(
            subject_c,
            message_c,
            from_e,
            [to_c],
            html_message=message_c,
        )

        # For employers

        subject_e = val.first_name+" applied for "+employer.job_title;

        message_e = render_to_string('employer_message.html', {
            'name': val.first_name + " "+val.last_name,
            'job_title': employer.job_title,
            'email' : val.email
        })

        to_e = employer.jobpostinguser.email;

        c = send_mail(
            subject_e,
            message_e,
            from_e,
            [to_e],
            html_message=message_e,
        )
        messages.add_message(request, messages.ERROR, 'Application Applied Sucessfully!')
        return HttpResponseRedirect('/');
    # def form_valid(self, form):
    #     form.instance.eemployee = self.request.user
    #     form.instance.employer = CompanyProfile.objects.get(pk =self.kwargs['string'])
    #     form.instance.job_app = JobPostingModel.objects.get(pk = self.kwargs['pk'])
    #     return super().form_valid(form);


class AboutView(TemplateView):
    template_name="home/about.html"


class PrivacyView(TemplateView):
    template_name="home/privacy.html"


class PressView(TemplateView):
    template_name="home/press.html"


class FAQView(TemplateView):
    template_name="home/faq.html"

class TermsView(TemplateView):
    template_name="home/terms.html"

class ContactView(CreateView):
    template_name = "home/contact.html"
    form_class = ContactModelForm;
    success_url = "/"



# from urllib.parse import urlencode
# from django import template
#
# register = template.Library()
#
# @register.simple_tag(takes_context=True)
# def url_replace(context, **kwargs):
#     query = context['request'].GET.dict()
#     query.update(kwargs)
#     return urlencode(query)
