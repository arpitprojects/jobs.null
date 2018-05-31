from .models import JobPostingModel;
from django import forms;
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class JobPostingModelForm(forms.ModelForm):

    job_description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    def clean_job_title(self):
        return self.cleaned_data['job_title'].capitalize()

    def clean_location(self):
        return self.cleaned_data['location'].capitalize()

    class Meta:
        model = JobPostingModel
        fields = ['job_title' , 'job_description' , 'notice_period' , 'location']



    def __init__(self, *args, **kwargs):
        super(JobPostingModelForm , self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
