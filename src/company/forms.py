from .models import CompanyProfile;
from django import forms;

class CompanyProfileForm(forms.ModelForm):

    class Meta:
        model = CompanyProfile
        exclude = ['commonuserprofile' , 'created_on', 'updated_on']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
