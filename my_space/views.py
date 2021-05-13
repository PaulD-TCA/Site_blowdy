from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from commerce.models import Product
from django.contrib.auth.models import User
from .forms import ProductsForm


# Create your views here.
def my_space(request):
    """Display the main web page."""
    template = loader.get_template('my_space/my_space_menu.html')
    context = {}
    return HttpResponse(template.render(context, request))

def upload_item(request):
    """Upload files for a design."""
    if request.method == 'POST':
        current_user = request.user.id
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            data_p_name = form.cleaned_data['p_name']
            data_p_description = form.cleaned_data['p_description']
            data_p_image = form.cleaned_data['p_image']
            data_p_category = form.cleaned_data['p_category']
            user_id = User.objects.get(id=request.user.id)
            data_to_save = Product(p_name=data_p_name,
                p_description=data_p_description, p_image=data_p_image,
                p_category=data_p_category, user_id=user_id)
            data_to_save.save()
            return redirect('home')
    else:
        form = ProductsForm()
    return render(request, 'my_space/upload_item.html', {'form':form})

def upload_article(request):
    """Upload files for a design."""
    if request.method == 'POST':
        current_user = request.user.id
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            data_p_name = form.cleaned_data['p_name']
            data_p_description = form.cleaned_data['p_description']
            data_p_image = form.cleaned_data['p_image']
            data_p_category = "Article"
            user_id = User.objects.get(id=request.user.id)
            data_to_save = Product(p_name=data_p_name,
                p_description=data_p_description, p_image=data_p_image,
                p_category=data_p_category, user_id=user_id)
            data_to_save.save()
            return redirect('home')
    else:
        form = ProductsForm()
    return render(request, 'my_space/upload_article.html', {'form':form})
