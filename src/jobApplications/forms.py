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

    class Meta:
        model = JobPostingModel
        fields = ['job_title' , 'job_description' , 'validity_in_months' , 'post_as_guest' , 'location']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
