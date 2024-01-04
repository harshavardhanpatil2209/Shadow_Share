"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views # here we are importing the views.py file of users app as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),  #this means whenever a user hits food/ url shift to the urls file of food app which will then access the views of the food app
    path('register/', user_views.register, name="register"),  #this means whenever a user hits food/ url shift to the urls file of food app which will then access the views of the food app
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),  
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),  
    path('profile/', user_views.profilepage, name="profile"),  
]


# this is done to make sure that the images are displayed on the website
from django.conf import settings   
from django.conf.urls.static import static

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
