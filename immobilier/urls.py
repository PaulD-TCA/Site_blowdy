from django.urls import path
from . import views

urlpatterns = [
    path('immobilier/', views.immobilier, name='immobilier'),
]
