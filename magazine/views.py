from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from commerce.models import Product



# Create your views here.
def magazine(request):
    """Display the main web page."""
    current_user = request.user.id
    articles = Product.objects.filter(p_category="Article")
    template = loader.get_template('magazine/magazine.html')
    context = {'articles':articles,}
    return HttpResponse(template.render(context, request))

def article_magazine(request, id):
    """Display an article page with a summary."""
    template = loader.get_template('magazine/article_magazine.html')
    articles_mag = Product.objects.filter(id=id)
    context = {'articles_mag':articles_mag,}
    return HttpResponse(template.render(context, request))
