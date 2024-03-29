from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from commerce.models import Product
from django.contrib.auth.models import User
# from .forms import ProductsForm



# Create your views here.
def bibliotheque(request):
    """Display the main web page."""
    template = loader.get_template('bibliotheque/livres_blo.html')
    context = {}
    return HttpResponse(template.render(context, request))

def bibliotheque_catalogue(request):
    """Display the main web page."""
    template = loader.get_template('bibliotheque/catalogue_livres.html')
    context = {}
    return HttpResponse(template.render(context, request))

def la_petite_princesse(request):
    """Display the main web page."""
    template = loader.get_template('bibliotheque/la_petite_princesse.html')
    context = {}
    return HttpResponse(template.render(context, request))

def gloire_et_richesses(request):
    """Display the main web page."""
    template = loader.get_template('bibliotheque/gloire_et_richesses.html')
    context = {}
    return HttpResponse(template.render(context, request))
