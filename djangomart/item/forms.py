from django import forms

from .models import Item

_custom_input_class = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select({
                'class': _custom_input_class
            }),
            'name': forms.TextInput({
                'class': _custom_input_class
            }),
            'description': forms.Textarea({
                'class': _custom_input_class
            }),
            'price': forms.TextInput({
                'class': _custom_input_class
            }),
            'image': forms.FileInput({
                'class': _custom_input_class
            })

        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput({
                'class': _custom_input_class
            }),
            'description': forms.Textarea({
                'class': _custom_input_class
            }),
            'price': forms.TextInput({
                'class': _custom_input_class
            }),
            'image': forms.FileInput({
                'class': _custom_input_class
            }),
            'is_sold': forms.CheckboxInput({
                'class': 'w-5 h-5 ml-3'
            })

        }