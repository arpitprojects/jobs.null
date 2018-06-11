from django.shortcuts import render ,HttpResponse , redirect
from django.views.generic import CreateView , TemplateView , DetailView , UpdateView , ListView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import JobPostingModelForm, JobPostingModelFormNew , JobPostingModelFormGuest
from .models import JobPostingModel
from accounts.models import CommonUserProfile
from accounts.decoraters import employer_required;
from django.utils.decorators import method_decorator
from itertools import chain
from accounts.models import CommonUserProfile
from company.models import CompanyProfile
from django.http import Http404
from .models import JobApply , JobPostingModel
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class PostJobAsGuest(CreateView):
    template_name = "jobposting/jop-post-as-guest.html"
    form_class = JobPostingModelFormGuest
    success_url = "/"


class ExploreJobs(ListView):
    template_name = "jobposting/index.html"
    queryset = JobPostingModel.objects.filter(is_active = True).order_by('-id')
    paginate_by = 5;
    count = 0;

    def get_context_data(self , *args, **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['count'] = self.count;
        context['query'] = self.request.GET.get('q')
        context['job_title'] = self.request.GET.get('job_title')
        context['location'] = self.request.GET.get('location')
        return context

    def get_queryset(self , *args , **kwargs):
        request = self.request;
        query = request.GET.get("q" , None)
        job_title = request.GET.get("job_title" , None);
        location = request.GET.get("location" , None);
        print('Flow :'+job_title);
        if query is not None:
            # print('Flow i hope we are not here');
            company_results = JobPostingModel.objects.search(query).filter(is_active = True)
            queryset_chain = chain(
                company_results
            )

            qs = sorted(queryset_chain , key = lambda instance : instance.pk , reverse = True)
            self.count= len(qs);
            return qs

        if job_title is not None and location is not None:
            # print('We must come here :'+job_title);
            company_results = JobPostingModel.objects.search_keywords(job_title , location).filter(is_active = True)
            queryset_chain = chain(
                company_results
            )

            qs = sorted(queryset_chain , key = lambda instance : instance.pk , reverse = True)
            self.count= len(qs);
            return qs

        if job_title is not None or location is not None:
            # print('we shall nor play this. :'+job_title);
            company_results = JobPostingModel.objects.search_keywords(job_title , location).filter(is_active = True)
            queryset_chain = chain(
                company_results
            )

            qs = sorted(queryset_chain , key = lambda instance : instance.pk , reverse = True)
            self.count= len(qs);
            return qs

        return JobPostingModel.objects.filter(is_active = True).order_by('-id')


@method_decorator([employer_required], name='dispatch')
class JobPostingView(LoginRequiredMixin , CreateView):
    form_class = JobPostingModelForm
    template_name = "jobposting/jobpost.html"
    success_url = '/'
    def form_valid(self, form):
        form.instance.jobpostinguser = self.request.user
        form.instance.jobposting = CompanyProfile.objects.get(pk = self.request.user)
        return super().form_valid(form);


    def get_context_data(self , **kwargs):
        # print(self.request.user)
        context = super(JobPostingView , self).get_context_data(**kwargs)
        context['condition'] = CompanyProfile.objects.filter(pk = self.request.user).values('name')
        print(context['condition']);
        return context

@method_decorator([employer_required] , name="dispatch")
class PreviousPostingsView(LoginRequiredMixin , ListView):
    template_name = "jobposting/prevous_post.html"
    paginate_by = 5
    count = 5;

    def get_queryset(self):
        pk = self.request.user
        queryset = JobPostingModel.objects.filter(jobpostinguser = pk).order_by('-pk');
        return queryset;


@method_decorator([employer_required] , name="dispatch")
class PreviousPostingsUpdateView(LoginRequiredMixin , UpdateView):
    model = JobPostingModel
    form_class = JobPostingModelForm
    template_name = "jobposting/jobpostingupdate.html"
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


@method_decorator([employer_required] , name="dispatch")
class ViewApplicationView(LoginRequiredMixin , ListView):
    template_name = "jobposting/view-applications.html"
    paginate_by = 5

    def get_queryset(self , *args , **kwargs):
        pk = self.kwargs['pk']
        queryset = JobApply.objects.filter(job_app = pk);
        return queryset;

@method_decorator([employer_required] , name="dispatch")
class ViewApplicationDeleteView(LoginRequiredMixin , DeleteView):
    model = JobApply;
    template_name = "jobposting/view-application-delete.html"

    def get_success_url(self):
        return '/jobs/view-applications/'+self.kwargs['superkey']+"/"

    def get_queryset(self):
        qs = super(ViewApplicationDeleteView, self).get_queryset()
        return qs.filter(id=self.kwargs['pk'])

@method_decorator([employer_required] , name="dispatch")
class ViewApplicationUpdateView(LoginRequiredMixin , UpdateView):
    model = JobApply
    template_name = "jobposting/view-applications-update.html"
    fields = ['status' , 'update_comment']
    def get_success_url(self):
        return '/jobs/view-applications/'+self.kwargs['superkey']+"/"

    def get_queryset(self , *args , **kwargs):
        qs = super(ViewApplicationUpdateView, self).get_queryset();
        return qs.filter(id=self.kwargs['pk'])
