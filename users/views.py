
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib import messages

# from .forms import UserRegistrationForm

# def home(request):
#     return render(request, 'users/home.html')

# def register(request):
#      
#         form = UserRegistratioForm(request.POST)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Your account has been created. You can log in now!')    
#             return redirect('login')

#     context = {'form': form}
#     return render(request, 'users/register.html', context)


from django.shortcuts import render, redirect
from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import  authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists') 
                return redirect('register')  
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('register')
    return render(request, 'auth/register.html')     

def login_page(request):
    userlogin = request.user
    if request.method == 'POST':
         username_var = request.POST.get('username')
         password_var = request.POST.get('password')
         user_profile = User.objects.filter(username=username_var)
         user = authenticate(request,username=username_var, password=password_var)
        
         if len(user_profile) < 1:
              messages.warning(request, 'This user does not exist')
         try:
             user_profile = User.objects.get(username=username_var)
         except:
             user_profile = None

         if user is not None and not user.check_password(password_var):
             messages.warning(request, "wrong password")
             
         elif user_profile is None:
             pass             
         if user :
            login(request, user)
            messages.success(request, 'Welcome '+ "" + str(userlogin))
            return redirect('home')            
    context = {}
    return render(request, 'auth/login.html', context)




def logout_page(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
                            
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=Profile.objects.get(user=request.user))
        
    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'auth/profile.html', context)    
       
                
    




