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
            data_design_name = form.cleaned_data['design_name']
            data_design_image = form.cleaned_data['design_image']
            data_plan_2d = form.cleaned_data['plan_2d']
            data_plan_3d = form.cleaned_data['plan_3d']
            data_assembly_instruction = form.cleaned_data['assembly_instruction']
            data_description = form.cleaned_data['description']
            data_category = form.cleaned_data['category']
            user = User.objects.get(id=request.user.id)
            data_to_save = Design(design_name=data_design_name,
                design_image=data_design_image, plan_2d=data_plan_2d,
                plan_3d=data_plan_3d, assembly_instruction=data_assembly_instruction,
                description=data_description, category=data_category, user_id=user)
            data_to_save.save()
            return redirect('home')
    else:
        form = ProductsForm()
    return render(request, 'my_space/upload_item.html', {'form':form})
