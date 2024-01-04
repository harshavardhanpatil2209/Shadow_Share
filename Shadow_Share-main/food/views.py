from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def index(request):   # i.e. this function is going to accept a particular user request
    item_list = Item.objects.all().reverse() # this is the list of all the items in the database which we have created in models.py of food app and we are reversing it so that the latest item comes first in the list
    # template  = loader.get_template('food/index.html')  # be careful with the path !! dont write complete path
    context = {
        'item_list' : item_list,
    }
    return render(request, 'food/index.html', context)

# class based views this view below is same as the above function based view 'index' [better way]
class IndexClassView(ListView): # inheriting from ListView
    model = Item
    template_name = 'food/index.html'
    # item_list = Item.objects.all()
    context_object_name = 'item_list'
    def get_queryset(self):
        return super().get_queryset().order_by('-id')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['image'] = Item.image.field.related_model
    #     return context
    
    #To get the latest post first, In the above code, we override the get_queryset() method and use the order_by() method to sort the queryset in descending order based on the id field. By prefixing the field name with a hyphen (-), we indicate that we want to sort in descending order. Now, when the item_list is retrieved, it will be reversed based on the id field.




def detail(request, item_id):  # we take item_id becoz its unique for every item ... this parameter is filled in the url
    item = Item.objects.get(pk = item_id)  # pk means primary key 
    context = {
        'item': item,
    }   
    return render(request, 'food/detail.html', context)


class FoodDetail(DetailView): # inheriting from DetailView
    model = Item
    template_name = 'food/detail.html'




def item(request):
    return HttpResponse('Another view!!')
def item1(request):
    return HttpResponse('ITem 1')
def item2(request):
    return HttpResponse('Item 2')

def create_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)  # this is the form which we have created in forms.py, its an object of ItemForm class and request.FILES is used to upload the image
    
    if form.is_valid():
        form.instance.user_name = request.user # here we are setting the user_name field of the form to the current user
        form.save()
        # form.instance.user_name = request.user 
        
        return redirect('food:index') # here index is the name of the url which we have created in urls.py of food app
    
    return render(request, 'food/item-form.html', {'form': form}) # this is the template which we have created in templates/food/item-form.html and context is the 'form' which we have created above


class CreateItem(CreateView): # inheriting from CreateView
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image', 'image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user # here we are setting the user_name field of the form to the current user
        return super().form_valid(form)



def update_item(request, id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
 # here instance is the item which we want to update because this data should already be present in the form
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form, 'item': item}) # this is the template which we have created in templates/food/item-form.html and context is the 'form' which we have created above

def delete_item(request, id):
    item = Item.objects.get(id = id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item': item}) # this is the template which we have created in templates/food/item-delete.html and context is the 'item' which we have created above