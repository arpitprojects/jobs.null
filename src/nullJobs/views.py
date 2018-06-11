from django.shortcuts import render ,HttpResponse , redirect , HttpResponseRedirect
from django.views.generic import CreateView , TemplateView , DetailView , UpdateView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from accounts.models import CommonUserProfile , SubscribeModel
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
from jobApplications.forms import JobApplyForm

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
        query = request.GET.get("q" , None);

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

# class AnonApply(CreateView):
#     model = JobApply;
#     queryset = JobApply.objects.all()
#     form_class =JobApplyForm
#


class AnonApply(View):
    def post(self, request , *args , **kwargs):
        # print(self.request);
        if not self.request.user.is_authenticated:
            name = self.request.POST.get("name")
            email = self.request.POST.get("email");
            message = self.request.POST.get("message");
            resume = self.request.FILES.get('resume' , False);
            # file = self.request.FILES['resume'];
            if not name or not email or not message or not resume:
                messages.add_message(request, messages.WARNING, 'You should fill all the inputs');
                return HttpResponseRedirect('/');
            else:
            # Later integrate the not twice posting funda
                status = JobApply.objects.filter(email = email ,  job_app  = (JobPostingModel.objects.get(pk = self.kwargs['pk']))).count();
                if status > 0:
                        messages.add_message(request, messages.WARNING, 'You have already applied for this job!')
                        return HttpResponseRedirect('/');
                else:

                    job_instance = JobPostingModel.objects.get(pk = self.kwargs['pk']);
                    jobapply = JobApply(email = email ,name = name  ,message = message ,upload_resume = resume , job_app = (JobPostingModel.objects.get(pk = self.kwargs['pk'])))
                    jobapply.save()

                    if job_instance.jobposting:
                        subject_c = 'Your application for '+job_instance.job_title+' at '+job_instance.jobposting.name+" is submitted"
                    else:
                        subject_c = 'Your application for '+job_instance.job_title+' at '+job_instance.company_name+" is submitted"

                    from_e = settings.EMAIL_HOST_USER

                    to_c = email

                    if job_instance.jobposting:
                        c_name = job_instance.jobposting.name;
                    else:
                        c_name = job_instance.company_name;


                    message_c = render_to_string('employee_message.html', {
                        'company_name': c_name,
                        'job_title': job_instance.job_title,
                    })


                    c = send_mail(
                        subject_c,
                        message_c,
                        from_e,
                        [to_c],
                        html_message=message_c,
                    )

                    # For employers

                    subject_e = name+" applied for "+job_instance.job_title;

                    message_e = render_to_string('employer_message.html', {
                        'name': name,
                        'job_title': job_instance.job_title,
                        'email' : email
                    })
                    if job_instance.jobposting:
                        to_e = job_instance.jobpostinguser.email;
                    else:
                        to_e = job_instance.company_email;


                    c = send_mail(
                        subject_e,
                        message_e,
                        from_e,
                        [to_e],
                        html_message=message_e,
                    )
                    messages.add_message(request, messages.ERROR, 'Application Applied Sucessfully!')
                    return HttpResponseRedirect('/');


@method_decorator([employee_required] , name="dispatch")
class ApplyView(View):
    def get(self , request , *args , **kwargs):

        if not self.request.user.is_authenticated:
            messages.add_message(request, messages.WARNING, 'Trigger jaavscript!')
            return HttpResponseRedirect('/');
        else:
            val = self.request.user; # User is logged here.

            # Check applied twice
            status = JobApply.objects.filter(employee = val , job_app  = (JobPostingModel.objects.get(pk = self.kwargs['pk']))).count();
            if status > 0:
                    messages.add_message(request, messages.WARNING, 'You have already applied for this job!')
                    return HttpResponseRedirect('/');
            else:
                employer = JobPostingModel.objects.get(pk = self.kwargs['pk']);
                #employer here us job
                # End of the email to the employee as well as employer
                jobapply = JobApply(employee = val ,job_app = (JobPostingModel.objects.get(pk = self.kwargs['pk'])))
                jobapply.save();

                #For employee
                # print(employer.jobposting.name)
                if  employer.jobposting:
                    subject_c = 'Your application for '+employer.job_title+' at '+employer.jobposting.name+" is submitted"
                else:
                    subject_c = 'Your application for '+employer.job_title+' at '+employer.company_name+" is submitted"

                from_e = settings.EMAIL_HOST_USER

                to_c = val.email

                if employer.jobposting:
                    c_name = employer.jobposting.name;
                else:
                    c_name = employer.company_name;


                message_c = render_to_string('employee_message.html', {
                    'company_name': c_name,
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
                if employer.jobposting:
                    to_e = employer.jobpostinguser.email;
                else:
                    to_e = employer.company_email;


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
