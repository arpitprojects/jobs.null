from .models import JobPostingModel , JobApply
from django import forms;
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class JobApplyForm(forms.ModelForm):

    class Meta:
        model = JobApply
        fields = ['name' , 'email' , 'message' , 'upload_resume']



    def __init__(self, *args, **kwargs):
        super(JobApplyForm , self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })


class JobPostingModelFormGuest(forms.ModelForm):

    job_description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': True, 'cols': 30, 'rows': 10}
        )
    )

    def clean_job_title(self):
        return self.cleaned_data['job_title'].capitalize()

    def clean_location(self):
        return self.cleaned_data['location'].capitalize()



    class Meta:
        model = JobPostingModel
        fields = [ 'job_type' , 'job_title' , 'job_description' , 'notice_period' , 'location' , 'company_name' , 'company_email' , 'company_website']



    def __init__(self, *args, **kwargs):
        super(JobPostingModelFormGuest , self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })



class JobPostingModelForm(forms.ModelForm):

    job_description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': True, 'cols': 30, 'rows': 10}
        )
    )

    def clean_job_title(self):
        return self.cleaned_data['job_title'].capitalize()

    def clean_location(self):
        return self.cleaned_data['location'].capitalize()

    class Meta:
        model = JobPostingModel
        fields = ['job_title' , 'job_description' , 'notice_period' , 'location' , 'job_type']



    def __init__(self, *args, **kwargs):
        super(JobPostingModelForm , self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })


class JobPostingModelFormNew(forms.ModelForm):

    job_description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': True, 'cols': 30, 'rows': 10}
        )
    )


    def clean_job_title(self):
        return self.cleaned_data['job_title'].capitalize()

    def clean_location(self):
        return self.cleaned_data['location'].capitalize()


    class Meta:
        model = JobPostingModel
        fields = "__all__"



    def __init__(self, *args, **kwargs):
        super(JobPostingModelFormNew , self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
