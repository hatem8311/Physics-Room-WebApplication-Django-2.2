from django import forms
from .models import User_Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=150, min_length=4)
    email = forms.EmailField(label='Enter Email')


    def clean_username(self):
        username1 = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username1)
        if r.count():
            raise ValidationError('user name already taken')
        return username1

    def clean_email(self):
        email1 = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email1)
        if r.count():
            raise ValidationError('email already taken')

        return email1

    #def clean_password2(self):
        #password1  =self.cleaned_data['password1']
        #password2 = self.cleaned_data['password2']
        #if password1 and password2 and password1 != password2:
            #raise ValidationError('Passwords do not match')
        #return password2

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'])
        return user



class Logging_in_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class userprofile_form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
            'first_name',
            'last_name',
            'age',
            'phone_number',
            'country',
            'city',
            'education',
            'profile_picture',
          ]
'''
class Email_Form(forms.Form):
    subject = forms.CharField(max_length=255)
    email = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    '''
class Email_Form(forms.Form):
    email = forms.CharField(required=True)
