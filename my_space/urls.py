from django.urls import path
from . import views

urlpatterns = [
    path('my_space/', views.my_space, name='my_space'),
    path('upload_item/', views.upload_item, name='upload_item'),
    path('upload_article/', views.upload_article, name='upload_article'),
]
