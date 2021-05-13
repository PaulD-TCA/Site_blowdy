from django.urls import path
from . import views

urlpatterns = [
    path('magazine/', views.magazine, name='magazine'),
    path('article_magazine/<int:id>/', views.article_magazine, name='article_magazine'),
]
