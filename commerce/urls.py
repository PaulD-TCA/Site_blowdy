from django.urls import path
from . import views

urlpatterns = [
    path('commerce/', views.commerce, name='commerce'),
    path('commerce/livres/', views.livres, name='livres'),
]
