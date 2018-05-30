from django.db import models
from accounts.models import CommonUserProfile;
from django.db.models import Q
# Create your models here.


class CompanyManager(models.Manager):

    def search(self , query =None):
        #queryset implemntation
        qs = self.get_queryset();
        if query is not None:
            or_lookup = (Q(name__icontains=query)  |
                Q(website__icontains=query) |
                Q(city__icontains = query) |
                Q(country__icontains = query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs


class CompanyProfile(models.Model):
    commonuserprofile = models.OneToOneField(CommonUserProfile , on_delete=models.CASCADE , primary_key = True)
    name = models.CharField(max_length =254)
    logo = models.ImageField(upload_to = 'media')
    website = models.URLField(max_length= 200)
    line1 = models.CharField(max_length = 100)
    line2 = models.CharField(max_length = 100)
    city = models.CharField(max_length=100)
    state =  models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    phone_line = models.DecimalField(max_digits = 10 , decimal_places=0 , default = 0000000000)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    objects = CompanyManager()

    def __str__(self):
        return self.name + " "+ self.website;
