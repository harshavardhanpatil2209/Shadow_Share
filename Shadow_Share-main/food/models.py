from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.  Models are created using a class . they are used to create database tables --- Each class represent a model 
class Item(models.Model):   # class Item is 'inherited' from class 'Model' --> inheritence in python

    def __str__(self):
        return self.item_name  #to directly get the names in Item.objects.all() while using shell
    

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # this is a foreign key which means that the user_name will be the primary key of the 'User' model and on_delete=models.CASCADE means that if the user is deleted then delete all the items of that user
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)
    # item_image = models.CharField(max_length=500, default="https://media4.giphy.com/media/26BRqPg05olzXG1bi/giphy.gif?cid=ecf05e47w7pu1wqd50xlfonrwvc45iat93zr1jlcmg39ft43&ep=v1_gifs_search&rid=giphy.gif&ct=g")
    image = models.ImageField(default='empty-box.gif', upload_to='posts')


    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk}) # here we are returning the url of the detail page of the item which we have created in urls.py of food app and kwargs={'pk': self.pk} means that the primary key of the item will be passed in the url
    
    
    

    # this will create a table with columns name, desc, price, etc and for that we need to add this food app in 'installed apps' section of settings.py and then migrate 
    #Whenever we add a model or changes we need to inform django by using command 'python manage.py makemigrations food'

    #at last to make a table -- run this command : "python manage.py sqlmigrate food "number that popped up in terminal" 
    # finally run the manage.py migrate command -- now the database table is actually created in the backend 

    # Now to work on the table -- adding data -- we shift to python shell by " python manage.py shell" and then create objects for this class which will be rows for the table ! Remember to save using obj_name.save()


    #Since this task is so tedious and lengthy, we use django admin to easily add update data -- command : "python manage.py createsuperuser"