from tinymce import HTMLField
from django.db import models
from company.models import CompanyProfile
from accounts.models import CommonUserProfile
from django.db.models import Q

# Create your models here.
PROFILE_CHOCES = (
    ('initated','Initiated'),
    ('no_response','no_response'),
    ('process','Process'),
    ('reject', 'Rejected'),
    ('hired', 'Hired'),
)


class JobPostingManager(models.Manager):

    def search(self , query =None):
        #queryset implemntation
        qs = self.get_queryset();
        if query is not None:
            or_lookup = (Q(job_title__icontains=query)  |
                Q(validity_in_months__icontains=query) |
                Q(location__icontains = query)|
                Q(jobposting__name__icontains = query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs



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

    objects  = JobPostingManager()

    def __str__(self):
        return self.job_title + " "+str(self.id);


class JobApply(models.Model):
    employee = models.ForeignKey(CommonUserProfile , on_delete = models.CASCADE)
    job_app = models.ForeignKey(JobPostingModel  , on_delete = models.CASCADE)
    update_comment = models.TextField(default = "PLease initaite the recruiting process!")
    status = models.CharField(max_length=22 , choices=PROFILE_CHOCES , default="initated" )
    created_on = models.DateTimeField(auto_now_add = True , null = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = (("employee", "job_app"),)

    def __str__(self):
        return str(self.employee.email  +" "+ self.job_app.job_title);
