from django import forms

from commerce.models import Product

class ProductsForm(forms.ModelForm):
    p_name = forms.CharField(max_length=30, required=False, help_text='Requis',
    widget=forms.TextInput(attrs={'placeholder': "Titre"}))
    p_description = forms.CharField(max_length=30, required=False, help_text='Requis',
    widget=forms.TextInput(attrs={'placeholder': "Description de l'article"}))

    class Meta:
        model = Product
        fields = ('p_name', 'p_description', 'p_image','p_category')

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)
