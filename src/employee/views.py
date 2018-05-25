
from django.shortcuts import render ,HttpResponse , redirect
from django.views.generic import CreateView , TemplateView , DetailView , UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import BasicEmployeeProfile ,EmployeeEducationDetails,EmployeeProfessionalDetails , EmployeeReusmeDetails;
from accounts.models import CommonUserProfile
from .forms import EmployeeDetailsForm , EmployeeEducationDetailsForm, EmployeeProfessionalDetailsForm , EmployeeReusmeDetailsForm;
from accounts.decoraters import employee_required;
from django.utils.decorators import method_decorator
from itertools import chain
# Create your views here.
# Create your views here.

@method_decorator([employee_required], name='dispatch')
class ProfileSettingsView(LoginRequiredMixin, UpdateView):
    form_class = EmployeeDetailsForm
    template_name = "basicemployee/profile_form.html"
    success_url = '/employee/education-details/'
    def form_valid(self, form):
        form.instance.employeeprofile = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        pk = self.request.user
        print(pk);
        obj, created = BasicEmployeeProfile.objects.get_or_create(employeeprofile = pk)
        return obj


@method_decorator([employee_required], name='dispatch')
class EmployeeEducationDetailsView(LoginRequiredMixin, UpdateView):
    form_class = EmployeeEducationDetailsForm;
    template_name = "basicemployee/profile_form.html"
    success_url = '/employee/professional-details/'

    def form_valid(self , form):
        form.instance.employeeprofile = self.request.user
        return super().form_valid(form)


    def get_object(self, queryset = None):
        pk = self.request.user;
        # print(pk);
        obj, created = EmployeeEducationDetails.objects.get_or_create(employeeeducationdetails = pk)
        return obj


@method_decorator([employee_required], name='dispatch')
class EmployeeProfessionalDetailsView(LoginRequiredMixin, UpdateView):
    form_class = EmployeeProfessionalDetailsForm;
    template_name = "basicemployee/professional_details.html"
    success_url = '/employee/resume/'

    def form_valid(self , form):
        form.instance.employeeprofessional = self.request.user
        return super().form_valid(form)


    def get_object(self, queryset = None):
        pk = self.request.user;
        obj, created = EmployeeProfessionalDetails.objects.get_or_create(employeeprofessional = pk)
        return obj

@method_decorator([employee_required], name='dispatch')
class EmployeeResumeDetailsView(LoginRequiredMixin, UpdateView):
    form_class = EmployeeReusmeDetailsForm;
    template_name = "basicemployee/resume.html"
    success_url = '/employee/resume/'

    def form_valid(self , form):
        form.instance.employeeresumedetails = self.request.user
        return super().form_valid(form)


    def get_object(self, queryset = None):
        pk = self.request.user;
        # print(pk)
        obj, created = EmployeeReusmeDetails.objects.get_or_create(employeeresumedetails = pk)
        return obj


class EmployeeProfileView(DetailView):
    template_name  = "basicemployee/profile.html"
    def get_queryset(self , queryset  = None):
        return  CommonUserProfile.objects.filter(slug=self.kwargs['slug']).values('id');

    def get_context_data(self, **kwargs):
        context = super(EmployeeProfileView, self).get_context_data(**kwargs)
        qs = CommonUserProfile.objects.filter(slug=self.kwargs['slug']).values('id');
        val  = qs[0]['id']
        context['initial'] =  CommonUserProfile.objects.filter(slug=self.kwargs['slug']).values('first_name' , 'last_name' , 'email' , 'last_login' , 'created_on')
        context['basic'] = BasicEmployeeProfile.objects.filter(employeeprofile__exact=val).values()
        context['prof'] = EmployeeProfessionalDetails.objects.filter(employeeprofessional=val).values()
        context['edu'] = EmployeeEducationDetails.objects.filter(employeeeducationdetails=val).values()
        context['resume'] = EmployeeReusmeDetails.objects.filter(employeeresumedetails=val).values()
        # print(context)
        return context
