from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm # here we are importing the UserRegisterForm which we have created in forms.py
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # here we are passing the data which user has entered in the form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # here we are getting the username which user has entered in the form
            messages.success(request, f'Account created for {username}!') # here we are displaying the message that account has been created
            return redirect('login') # here login is the name of the url which we have created in urls.py of users app and we are redirecting the user to login page after successful registration
        
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form}) # here we are passing the form to the register.html template
@login_required # this decorator is used to make sure that the user is logged in before accessing the profile page
def profilepage(request):
    return render(request, 'users/profile.html') # here we are passing the form to the profile.html template