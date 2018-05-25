from django.db import models
import datetime
from .validators import validate_file_extension
from accounts.models import CommonUserProfile;
# Create your models here.
P_PLACE = (
    ('Pune' , 'Pune'),
    ('Mumbai' , 'Mumbai'),
    ('Kolkata' , 'Kolkata'),
    ('Hyderabad' , 'Hyderabads'),
    ('Banglore' , 'Banglore'),
    ('Delhi' , 'Delhi'),
    ('Gurugram' , 'Gurugram'),
    ('Jaipur' , 'Jaipur')
)

CHOICES = (
    ('Salaried' , 'Salaried'),
    ('Jobless' , 'Jobless'),
    ('Freelance' , 'Freelance'),
    ('Contract' , 'Contract'),
);
DEGREE = (
    ('Secondary School' , 'Secondary School'),
    ('Higher Secondary' , 'Higher Secondary'),
    ('Graduation' , 'Graduation'),
    ('Post Graduation' , 'Post Graduation'),
);

class BasicEmployeeProfile(models.Model):
    employeeprofile = models.OneToOneField(CommonUserProfile , on_delete=models.CASCADE , primary_key = True)
    current_city = models.CharField(max_length = 100)
    picture = models.ImageField(upload_to = "media" , blank=True, null=True)
    age = models.DecimalField(max_digits = 3 , decimal_places=0 , default = 0)
    address_line1 = models.CharField(max_length = 100)
    address_line2 = models.CharField(max_length=100)
    preffered_place  = models.CharField(max_length = 100 , choices= P_PLACE )
    current_status = models.CharField(max_length = 40 , choices= CHOICES , default = 'JObless')
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def  __str__(self):
        return str('Details of '+self.employeeprofile.email);


class EmployeeEducationDetails(models.Model):
    employeeeducationdetails = models.OneToOneField(CommonUserProfile , on_delete=models.CASCADE , primary_key = True)
    degree = models.CharField(max_length = 100 , choices= DEGREE , default="Secondary School")
    board = models.CharField(max_length = 100 ,default =" ")
    grade_cgpa = models.CharField(max_length = 100 , default = 0)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    def  __str__(self):
        return str("Education of "+self.employeeeducationdetails.email);


class EmployeeProfessionalDetails(models.Model):
    employeeprofessional = models.OneToOneField(CommonUserProfile , on_delete=models.CASCADE , primary_key = True)
    previous_compnay_name = models.CharField(max_length = 255)
    date_of_joining = models.DateField(default = datetime.date.today)
    date_of_leaving = models.DateField(default = datetime.date.today)
    notice_period_in_months = models.DecimalField(max_digits = 3 , decimal_places= 0 , default=0)
    current_ctc = models.DecimalField(max_digits = 10 , decimal_places = 2 , default=0)
    expected_ctc = models.DecimalField(max_digits = 10 , decimal_places = 2 , default=0)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def  __str__(self):
        return str("Previous Job of "+self.employeeprofessional.email);


class EmployeeReusmeDetails(models.Model):
    employeeresumedetails = models.OneToOneField(CommonUserProfile , on_delete=models.CASCADE , primary_key = True)
    upload_resume = models.FileField(upload_to="media" , validators=[validate_file_extension])
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "Resume of "+self.employeeresumedetails.email;
