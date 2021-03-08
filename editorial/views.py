from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def home(request):
    """Display the main web page."""
    template = loader.get_template('editorial/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def user_login(request):
    """Allow users to login to an account."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nom utilisateur ou mot de passe incorrect')
    context = {}
    return render(request, 'editorial/login.html', context)


def user_logout(request):
    """Allow users to logout of an account."""
    logout(request)
    return redirect('home')


def user_signup(request):
    """Allow users to create an account."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Le compte à été créé')
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'editorial/signup.html', {'form': form})
