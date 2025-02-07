from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns=[
    path('',views.home,name='home'),
    path('view/<int:pk>',views.viewvehicle,name='view'),
    path('vehicle/<str:type>/',views.vehicle,name='vehicle'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('postads',views.postAds,name="postads"),
    path('resetpwd',views.pwdReset,name="pwdReset"),
    path('logout',views.logout,name="logout"),
    path('updateuser',views.updateuser,name='updateuser'),
    path('profile',views.profile,name="profile"),
    path('deletepost/<int:pk>',views.deletepost,name="deletepost"),
    path('updatepost/<int:pk>',views.updatepost,name="updatepost"),
    path('deleteuser',views.deleteuser,name="deleteuser"),
    path('contact',views.contact,name="contact"),
    path('faq',views.faq,name="faq"),
    path('terms & conditions',views.terms,name="terms"),
    path('aboutus',views.aboutus,name="aboutus"),
    path(
        'password_reset/',
        auth_view.PasswordResetView.as_view(template_name="password_reset.html"),
        name="password_reset",
    ),
    path(
        'password_reset_done/',
        auth_view.PasswordResetDoneView.as_view(template_name="password_done.html"),
        name="password_reset_done",
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        auth_view.PasswordResetConfirmView.as_view(template_name="password_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        'password_reset_complete/',
        auth_view.PasswordResetCompleteView.as_view(template_name="password_comple.html"),
        name="password_reset_complete",
    ),

    
]