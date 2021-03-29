from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product
from django.contrib.auth.models import User


# Create your views here.
def commerce(request):
    """Display the main web page."""
    template = loader.get_template('commerce/commerce.html')
    context = {}
    return HttpResponse(template.render(context, request))

def livres(request):
    """Display user saved foods."""
    # current_user = request.user.id
    favourites_list = Product.objects.filter()
    template = loader.get_template('commerce/livres.html')
    context = {'favourites_list':favourites_list}
    return HttpResponse(template.render(context, request))
