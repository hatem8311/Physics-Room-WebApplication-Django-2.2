from django.urls import path
from .views import (
    creat_user_view,
    login_user_view,
    userprofile_view,
    resetpassowrd_view,
    set_pass_view,
    profile_view,
logout_view)
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [

    path('register/' , creat_user_view),
    path('login/' ,login_user_view),
    path('updateprofile/' , userprofile_view , name ='updatingprofile'),
    path('changepass/' ,resetpassowrd_view),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password-reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/pass_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/pass_reset_confirm.html'),name='password_reset_confirm'),
    #path('contact/',contact_view),
    path('set/',set_pass_view  ),
    path('profile/<int:my_id>' , profile_view),
    path('logout/',logout_view)




]