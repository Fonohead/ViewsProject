from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'description',
            'quantity',
            'price',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description is not None and len(description) < 20:
            raise ValidationError({'description': 'Описание не может быть меньше 20 символов!'})

        name = cleaned_data.get('name')
        if name == description:
            raise ValidationError({'name': 'Название не должно совпадать с описанием!'})

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].islower():
            raise ValidationError({'name': 'Название должно начинаться с заглавной буквы!'})
        return name
