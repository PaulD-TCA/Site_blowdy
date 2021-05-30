from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('magazine/', views.magazine, name='magazine'),
    path('article_magazine/<int:id>/', views.article_magazine, name='article_magazine'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
