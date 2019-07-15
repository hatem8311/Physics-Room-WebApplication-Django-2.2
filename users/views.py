from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import Logging_in_form , userprofile_form , Email_Form,CustomUserCreationForm
from django.contrib import messages
from .models import User_Profile
from django.contrib.auth import login , authenticate ,update_session_auth_hash,logout

def creat_user_view(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.set_password('kadjgksfgoj%sfd46547FDG5447' %(instance.email))
            instance.save()
            return redirect('/users/set/')



    else:
        form =CustomUserCreationForm()

    context = {'form':form}
    return  render(request , 'users/create_user_form.html', context)

def login_user_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:updatingprofile'))
    form = Logging_in_form()
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login succesfully')
            return redirect('/')






    context = {'form':form}
    return  render(request,'users/logging_in.html',context)

@login_required(redirect_field_name='/users/login')
def userprofile_view(request):
    form =userprofile_form(instance=request.user.user_profile)
    if request.method =='POST':
        ##instance in the line below os to avoid an error related to  id
        form = userprofile_form(request.POST,request.FILES,instance=request.user.user_profile )
        if form.is_valid():
            print(request.POST)
            form.save()
            return HttpResponse('operation done succefully')
    context = {'form':form}
    return render(request,'users/profile_creation.html' , context)

def resetpassowrd_view(request):
    form = PasswordChangeForm(user=request.user)
    if request.method =='POST':
        form = PasswordChangeForm(user=request.user , data=request.POST)
        if form.is_valid():
            form.save()
            print(form.user)
            update_session_auth_hash(request , form.user)
            messages.success(request  , 'password changed successfully')
    context = {'form':form}
    return render(request , 'users/password_reset_loggedin.html' , context)


def set_pass_view(request):
    return render(request,'users/set_pass.html')


@login_required(redirect_field_name='/users/login')
def profile_view(request, my_id):
    user = get_object_or_404(User_Profile, id=my_id)
    context={'user': user}
    return render(request,'users/profile.html',context)


@login_required(redirect_field_name='/users/login')
def logout_view(request):
    logout(request)
    return redirect(reverse('success'))
'''
def contact_view(request):
    form = Email_Form()
    if request.method=='POST':
        form = Email_Form(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = 'welcome to our site'
            subject = 'welcome'
            send_mail(subject ,message , settings.EMAIL_HOST_USER , [email])
    context = {'form':form}
    return render(request , 'users/contact.html' , context)
'''

