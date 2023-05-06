from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Register', views.registration, name='register'),
    path('Login', views.login, name='login'),
    path('Logout', views.logout, name='logout'),
    path('User_Details', views.details, name='userdetails'),
    path('Customer_Redirect_Registration', views.redirect_registration, name='custredirect')
]
