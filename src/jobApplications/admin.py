from django.contrib import admin
from .models import JobPostingModel , JobApply
# Register your models here.

admin.site.register(JobPostingModel);
admin.site.register(JobApply)
