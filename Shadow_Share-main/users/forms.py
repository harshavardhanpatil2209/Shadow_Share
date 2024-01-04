from django import forms
from django.contrib.auth.models import User # here we are importing the User model to inherit from it
from django.contrib.auth.forms import UserCreationForm # here we are importing the UserCreationForm to inherit from it

class UserRegisterForm(UserCreationForm): # here we are inheriting from UserCreationForm
    email = forms.EmailField() # here we are adding a new field to the form
    
    
    class Meta: # this class is going to work for userregisterform class and is going to provide some extra functionality such as adding new fields
        model = User # here we are telling that this form is going to interact with User model
        fields = ['username', 'email', 'password1', 'password2'] # here we are telling which fields we want to display in the form
         