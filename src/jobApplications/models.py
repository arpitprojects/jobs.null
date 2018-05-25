from tinymce import HTMLField
from django.db import models
from company.models import CompanyProfile
from accounts.models import CommonUserProfile

# Create your models here.
class JobPostingModel(models.Model):
    jobposting = models.ForeignKey(CompanyProfile , on_delete=models.CASCADE , related_name="company_matching")
    jobpostinguser = models.ForeignKey(CommonUserProfile , on_delete=models.CASCADE , related_name = "user_matching")
    is_active = models.BooleanField(default = False)
    job_title = models.CharField(max_length = 255)
    job_description = HTMLField('Content')
    validity_in_months = models.DecimalField(max_digits = 4 , decimal_places = 0 , default = 0)
    post_as_guest = models.BooleanField(default = False)
    location = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add = True , null = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.job_title + " "+str(self.id);


class JobApply(models.Model):
    employee = models.ForeignKey(CommonUserProfile , on_delete = models.CASCADE)
    job_app = models.ForeignKey(JobPostingModel  , on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True , null = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = (("employee", "job_app"),)

    def __str__(self):
        return str(self.employee.email  +" "+ self.job_app.job_title);
