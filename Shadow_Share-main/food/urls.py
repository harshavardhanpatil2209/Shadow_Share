from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(), name = 'index'),  # index is the function name in views.py and whenever user hits that empty url after food/ he should be able to see the view created in views.py
    #/food/1 or 2 etc
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    path('item1/', views.item1, name='item1'),
    path('item2/', views.item2, name='item2'),
    #/food/add # this is the url which we have to hit to add a new item
    path('add/', views.create_item, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'), # this is the url which we have to hit to update an item ... here id is the primary key of the item which we want to update
    path('delete/<int:id>/', views.delete_item, name='delete_item'), # this is the url which we have to hit to delete an item ... here id is the primary key of the item which we want to delete
]
