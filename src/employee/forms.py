from .models import BasicEmployeeProfile , EmployeeEducationDetails, EmployeeProfessionalDetails , EmployeeReusmeDetails
from django import forms;
import datetime
class EmployeeEducationDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeEducationDetails
        fields = ['degree' , 'board' , 'grade_cgpa']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        });

class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = BasicEmployeeProfile
        exclude = ['employeeprofile']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        });

class EmployeeProfessionalDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfessionalDetails
        fields = ['previous_compnay_name' ,  'date_of_joining' , 'date_of_leaving' , 'notice_period_in_months' , 'current_ctc' , 'expected_ctc']
        widgets = {
            'date_of_joining': DateInput(),
            'date_of_leaving' : DateInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        });


class EmployeeReusmeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeReusmeDetails;
        fields = ['upload_resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        });
