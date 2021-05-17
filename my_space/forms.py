from django import forms

from commerce.models import Product

category_choice= [
    ('Livre', 'Livre'),
#    ('Article', 'Article'),
    ('Immobilier', 'Immobilier'),
    ]


class ProductsForm(forms.ModelForm):
    p_name = forms.CharField(max_length=30, required=False, help_text='Requis',
    widget=forms.TextInput(attrs={'placeholder': "Titre"}))
    p_summary = forms.CharField(max_length=300, required=False, help_text='Requis',
    widget=forms.TextInput(attrs={'placeholder': "Résumé"}))
    p_description = forms.CharField(max_length=7500, required=False, help_text='Requis',
    widget=forms.Textarea(attrs={'placeholder': "Article"}))
    p_category = forms.CharField(label='What is your favorite fruit?', required=False, help_text='Requis',
    widget=forms.Select(choices=category_choice))#(attrs={'placeholder': "Catégorie" }))

    class Meta:
        model = Product
        fields = ('p_name', 'p_summary', 'p_description', 'p_image','p_category')

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)
