from django.contrib import admin
from .models import BasicEmployeeProfile , EmployeeEducationDetails , EmployeeProfessionalDetails , EmployeeReusmeDetails;
# Register your models here.
admin.site.register(BasicEmployeeProfile);
admin.site.register(EmployeeEducationDetails);
admin.site.register(EmployeeProfessionalDetails);
admin.site.register(EmployeeReusmeDetails);
