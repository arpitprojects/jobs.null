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
            company_results = JobPostingModel.objects.search(query)
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
    # fields = '__all__'
    # template_name = "jobposting/jobapply_form.html"
    def get(self , request , *args , **kwargs):
        val = self.request.user
        jobapply = JobApply(employee = val ,job_app = (JobPostingModel.objects.get(pk = self.kwargs['pk'])))
        jobapply.save();
        messages.add_message(request, messages.ERROR, 'Application Applied Sucessfully!')
        return HttpResponseRedirect('/');
    # def form_valid(self, form):
    #     form.instance.eemployee = self.request.user
    #     form.instance.employer = CompanyProfile.objects.get(pk =self.kwargs['string'])
    #     form.instance.job_app = JobPostingModel.objects.get(pk = self.kwargs['pk'])
    #     return super().form_valid(form);
