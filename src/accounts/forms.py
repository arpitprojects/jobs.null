from .models import CommonUserProfile;
from django import forms;

class CommonUserProfileLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CommonUserProfile
        fields = ['email' , 'password']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })


class CommonUserProfileRegisterForm(forms.ModelForm):
    confirm_password =  forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    # profile_type = forms.CharField(label="" , widget=forms.RadioSelect(attrs={'placeholder' : "Your tweet" , 'class' : 'form-control' }))
    class Meta:
        model = CommonUserProfile
        fields = ['first_name' , 'last_name' , 'email' , 'profile_type' , 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
