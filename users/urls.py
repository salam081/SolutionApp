from django.urls import path
from users.views import *



urlpatterns = [
    path('',login_page, name='login'),
    path('logout/',logout_page, name='logout'),
    path('register/',register, name='register'),
   

]