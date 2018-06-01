from django.shortcuts import render ,HttpResponse , redirect
from django.views.generic import CreateView , TemplateView , DetailView
from .models import CommonUserProfile
from .forms import CommonUserProfileLoginForm , CommonUserProfileRegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login , logout
from django.conf import settings
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy
import datetime
# From email activation
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
# End of email activtion


class LoginView(CreateView):
    form_class = CommonUserProfileLoginForm
    template_name = "accounts/login.html"

    def post(self , request):
        username = request.POST['email'];
        password = request.POST['password'];

        user = authenticate(username = username , password = password);
        # print(user);
        if user is not None:
            if user.is_active:
                login(request , user);
                # print(user.id);
                # messages.add_message(self.request, messages.INFO, 'User Logged in SuccessFully!')
                print(user.profile_type);
                next = request.GET.get('next', None)
                if next:
                    # See caution note below!
                    return redirect(next)
                if user.profile_type == "employee" or user.profile_type == False:
                    return redirect('/employee/details/')
                else:
                    return redirect('/company/profile-settings/')
            else:
                # messages.add_message(self.request, messages.ERROR, 'Your are not an active user!')
                messages.add_message(request, messages.ERROR, 'You are not activated by admin!')
        else:
            # messages.add_message(self.request, messages.ERROR, 'Your are not an active user!')
            messages.add_message(request, messages.ERROR, 'You are not a user, Please Register!')

        return redirect( '/accounts/login');


class RegisterView(CreateView):
    form_class = CommonUserProfileRegisterForm
    template_name = "accounts/register.html"

    def post(self , request):
        email = request.POST['email'];
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        profile_type = request.POST['profile_type']

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
             messages.add_message(request, messages.ERROR, 'Confirm Password you entered is not matching!')
             return redirect( '/accounts/register');
        else:
            if not CommonUserProfile.objects.filter(email = email).exists():
                user = CommonUserProfile.objects.create_user(email = email , first_name = first_name , last_name = last_name , profile_type = profile_type  ,password = password )
                # print('Printing some attributes');
                #
                # print(urlsafe_base64_encode(force_bytes(user.pk)));
                # print(user);
                # print('End of values print');

                current_site = get_current_site(request)
                subject = 'Activate Your NUll Jobs Account'
                from_e = settings.EMAIL_HOST_USER
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                # print('Printing some attributes');
                # print(message);
                # print(from_e)
                # print('Printing some attributes');
                temp_message = "just a mesag"
                c = send_mail(
                    subject,
                    message,
                    from_e,
                    [email],
                    html_message=message,
                )
                print('Printing some attributes');
                print(c)
                print('Printing some attributes');
                return redirect('/accounts/account_activation_sent/');
                # user = authenticate(username = email , password = password);
                # login(request , user);
                # if user.profile_type == "employee":
                #     return redirect('/employee/details/')
                # else:
                #     return redirect('/company/profile-settings/')
                # return HttpResponse('OK');
            else:
                messages.add_message(request, messages.ERROR, 'User Already Exists!')
                return redirect( '/accounts/register');



class LogoutView(View):
    def get(self , request):
        logout(request);

        return redirect('/accounts/login/')

class AccountActivationView(TemplateView):
    template_name = "accounts/activation.html"


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CommonUserProfile.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('Something broken!');
