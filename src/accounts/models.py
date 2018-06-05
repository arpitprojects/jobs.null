from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from slugify import slugify
from django.utils.text import slugify
import uuid
# Create your models here.
PROFILE_CHOCES = (
    ('employee','Employee'),
    ('employer', 'Employer'),
)
class CommonUserProfileManager(BaseUserManager):
    def create_user(self,email , first_name , last_name,  profile_type , password = None):
        if not email:
            raise ValueError("Email is needed!");
        email = self.normalize_email(email);
        user = self.model(email = email , first_name = first_name  , last_name = last_name , profile_type = profile_type)
        user.set_password(password);
        user.save(using = self._db);
        return user;


    def create_superuser(self , email , first_name , last_name , profile_type , password):
        user = self.create_user(email , first_name , last_name , profile_type  , password);
        user.is_superuser = True;
        user.save(using = self._db);
        return user;


class CommonUserProfile(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=255 , unique = True)
    slug = models.SlugField(max_length = 255 , unique = True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = True)
    profile_type = models.CharField(max_length=8 , choices=PROFILE_CHOCES , default="employee" )
    #default is taking as employee
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)


    objects = CommonUserProfileManager();

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name' , 'last_name' , 'profile_type']

    def __str__(self):
        return  self.email

    def __unicode__(self):
        if self.profile_type == True:
            type_user = "Employee"
        else:
            type_user = "Employer"

        return '{}  - {}'.format(type_user ,  self.email);


    def get_full_name(self):
        return '{}{}'.format(self.first_name , self.last_name)

    def get_short_name(self):
        return self.first_name;

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(uuid.uuid4().hex)

        super(CommonUserProfile, self).save(*args, **kwargs)



class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.email+ " "+ self.subject;
