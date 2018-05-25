from django.shortcuts import render ,HttpResponse , redirect
from django.views.generic import CreateView , TemplateView , DetailView , UpdateView , ListView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import JobPostingModelForm
from .models import JobPostingModel
from accounts.models import CommonUserProfile
from accounts.decoraters import employer_required;
from django.utils.decorators import method_decorator
from itertools import chain
from accounts.models import CommonUserProfile
from company.models import CompanyProfile
from django.http import Http404
# Create your views here.

@method_decorator([employer_required], name='dispatch')
class JobPostingView(LoginRequiredMixin , CreateView):
    form_class = JobPostingModelForm
    template_name = "jobposting/jobpost.html"
    success_url = '/'
    def form_valid(self, form):
        form.instance.jobpostinguser = self.request.user
        form.instance.jobposting = CompanyProfile.objects.get(pk = self.request.user.id)
        return super().form_valid(form);

    # def get_object(self, queryset=None):
    #     # pk = self.request.user.id;
    #     # print(pk);
    #     created = JobPostingModel.objects.create()

@method_decorator([employer_required] , name="dispatch")
class PreviousPostingsView(LoginRequiredMixin , ListView):
    template_name = "jobposting/prevous_post.html"
    paginate_by = 5

    def get_queryset(self):
        pk = self.request.user
        # print(pk);
        queryset = JobPostingModel.objects.filter(jobpostinguser = pk);
        return queryset;


@method_decorator([employer_required] , name="dispatch")
class PreviousPostingsUpdateView(LoginRequiredMixin , UpdateView):
    model = JobPostingModel
    form_class = JobPostingModelForm
    template_name = "jobposting/jobpostingupdate.html"
    # fields = ['job_title' , 'job_description' , 'validity_in_months' , 'post_as_guest',  'location']
    success_url = "/jobs/previous-posts"
    def get_queryset(self):
        qs = super(PreviousPostingsUpdateView, self).get_queryset();
        return qs.filter(jobpostinguser=self.request.user.id)


@method_decorator([employer_required] , name="dispatch")
class PreviousPostingsDeleteView(LoginRequiredMixin , DeleteView):
    model = JobPostingModel;
    template_name = "jobposting/post_delete.html"
    success_url = "/jobs/previous-posts"
    def get_queryset(self):
        qs = super(PreviousPostingsDeleteView, self).get_queryset()
        return qs.filter(jobpostinguser=self.request.user.id)
