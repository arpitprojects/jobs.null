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
                Q(notice_period__icontains=query) |
                Q(location__icontains = query)|
                Q(jobposting__name__icontains = query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs

    def search_keywords(self , job_title = None , location = None):
        qs = self.get_queryset();
        # print('We shoulf come herfe'+location+job_title);
        if job_title is not None and location is not None:
            print('Are wee here');
            or_lookup = (Q(job_title__icontains = job_title)
            & Q(location__icontains = location)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs

        if job_title is not None or location is not None:
            # print('i am not here');
            or_lookup = (Q(job_title__icontains = job_title) |
                        Q(location__icontains = location)
                    )
            qs = qs.filter(or_lookup).distinct()

        return qs


class JobPostingModel(models.Model):
    jobposting = models.ForeignKey(CompanyProfile , on_delete=models.CASCADE , related_name="company_matching")
    jobpostinguser = models.ForeignKey(CommonUserProfile , on_delete=models.CASCADE , related_name = "user_matching")
    is_active = models.BooleanField(default = False)
    job_title = models.CharField(max_length = 255)
    job_description = HTMLField('Content')
    notice_period = models.CharField(max_length = 30)
    location = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add = True , null = True)
    updated_on = models.DateTimeField(auto_now = True)

    objects  = JobPostingManager()

    def __str__(self):
        return self.job_title + "@"+"Active Status : "+str(self.is_active);


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
        return str(self.employee.email  +" "+ self.job_app.job_title)
