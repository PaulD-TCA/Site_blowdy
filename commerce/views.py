from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def commerce(request):
    """Display the main web page."""
    template = loader.get_template('commerce/commerce.html')
    context = {}
    return HttpResponse(template.render(context, request))
