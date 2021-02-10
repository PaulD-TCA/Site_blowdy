from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    """Display the main web page."""
    template = loader.get_template('editorial/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
