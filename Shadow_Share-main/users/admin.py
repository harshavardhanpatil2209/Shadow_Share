from django.contrib import admin
from .models import Profile # here we are importing the Profile model from models.py file of users app
# Register your models here.

admin.site.register(Profile) # here we are registering the Profile model so that it can be seen in the admin page