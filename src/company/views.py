from django.shortcuts import render ,HttpResponse , redirect, get_object_or_404
from django.views.generic import CreateView , TemplateView , DetailView , UpdateView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import CompanyProfileForm
from .models import CompanyProfile
from accounts.models import CommonUserProfile
from accounts.decoraters import employer_required;
from django.utils.decorators import method_decorator
from itertools import chain

# Create your views here.

@method_decorator([employer_required], name='dispatch')
class ProfileSettingsView(LoginRequiredMixin , UpdateView):
    form_class = CompanyProfileForm
    is_update_view = True
    template_name = "company/profile-settings.html"
    success_url = '/company/profile-settings/'
    def form_valid(self, form):
        if form.is_valid():
            form.instance.commonuserprofile = self.request.user
            return super().form_valid(form)

    def get_object(self, queryset=None):
        # print(commonuserprofile);
        # print(self.kwargs[commonuserprofile])
        pk = self.request.user
        obj, created = CompanyProfile.objects.get_or_create(commonuserprofile = pk)
        return obj


class CompanyListView(ListView):
    model = CompanyProfile
    paginate_by = 10
    template_name = "company/compnay-list.html"
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
            company_results = CompanyProfile.objects.search(query)

            queryset_chain = chain(
                company_results
            )

            qs = sorted(queryset_chain , key = lambda instance : instance.pk , reverse = True)
            self.count= len(qs);
            return qs

        return CompanyProfile.objects.none()
