from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model): # here we are creating a new model named Profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) # here we are creating a one to one relationship with User model and on_delete=models.CASCADE means if the user is deleted then delete the profile also
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # upload_to='profile_pics' means that the images will be stored in profile_pics folder inside media folder
    location = models.CharField(max_length=100, default='India')

    def __str__(self):
        return f'{self.user.username} Profile' # here we are returning the username of the user and profile  
