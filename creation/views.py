from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from commerce.models import Product
from django.contrib.auth.models import User


# Create your views here.
def creation(request):
    """Display the main web page."""
    template = loader.get_template('creation/creation.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aura_chromatic(request):
    """Display the main web page."""
    template = loader.get_template('creation/aura_chromatic.html')
    context = {}
    return HttpResponse(template.render(context, request))


def aura_chromatic_2(request):
    """Display the main web page."""
    template = loader.get_template('creation/aura_chromatic_2.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Debacle_polaire(request):
    """Display the main web page."""
    template = loader.get_template('creation/Debacle_polaire.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Echos_d_ames(request):
    """Display the main web page."""
    template = loader.get_template('creation/Echos_d_ames.html')
    context = {}
    return HttpResponse(template.render(context, request))


def La_fleur_verte_de_Sylvie(request):
    """Display the main web page."""
    template = loader.get_template('creation/La_fleur_verte_de_Sylvie.html')
    context = {}
    return HttpResponse(template.render(context, request))


def L_ecrivain(request):
    """Display the main web page."""
    template = loader.get_template('creation/L_ecrivain.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Lex_o_Mille(request):
    """Display the main web page."""
    template = loader.get_template('creation/Lex_o_Mille.html')
    context = {}
    return HttpResponse(template.render(context, request))


def L_inconstance(request):
    """Display the main web page."""
    template = loader.get_template('creation/L_inconstance.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Lumiere_a_l_horizon(request):
    """Display the main web page."""
    template = loader.get_template('creation/Lumiere_a_l_horizon.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Old_vintage(request):
    """Display the main web page."""
    template = loader.get_template('creation/Old_vintage.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Spirale(request):
    """Display the main web page."""
    template = loader.get_template('creation/Spirale.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Stigmate_3(request):
    """Display the main web page."""
    template = loader.get_template('creation/Stigmate_3.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Symphonie_de_rue(request):
    """Display the main web page."""
    template = loader.get_template('creation/Symphonie_de_rue.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Une_vie_representee(request):
    """Display the main web page."""
    template = loader.get_template('creation/Une_vie_representee.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Vue_de_l_espace(request):
    """Display the main web page."""
    template = loader.get_template('creation/Vue_de_l_espace.html')
    context = {}
    return HttpResponse(template.render(context, request))
