from django import forms
from .models import Item

class ItemForm(forms.ModelForm):  # this is a class which is inheriting from forms.ModelForm
    class Meta:
        model = Item # this is the model which we are going to use
        fields = [         # these are the fields which we want to display in the form
            'item_name',
            'item_desc',
            # 'item_price',
            # 'item_image',
            'image',
        ]
        
        # widgets = {
        #     'item_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'item_desc': forms.Textarea(attrs={'class': 'form-control'}),
        #     'item_price': forms.TextInput(attrs={'class': 'form-control'}),
        #     'item_image': forms.TextInput(attrs={'class': 'form-control'}),
        # }