"""mdem_s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('editorial.urls')),
    path('editorial/', include('editorial.urls')),
    path('', include('commerce.urls')),
    path('commerce/', include('commerce.urls')),
    path('', include('immobilier.urls')),
    path('immobilier/', include('immobilier.urls')),
    path('', include('my_space.urls')),
    path('my_space/', include('my_space.urls')),
    path('', include('magazine.urls')),
    path('magazine/', include('magazine.urls')),
]
