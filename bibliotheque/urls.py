from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bibliotheque/', views.bibliotheque, name='bibliotheque'),
    path('bibliotheque_catalogue/', views.bibliotheque_catalogue, name='bibliotheque_catalogue'),
    path('la_petite_princesse/', views.la_petite_princesse, name='la_petite_princesse'),
    path('gloire_et_richesses/', views.gloire_et_richesses, name='gloire_et_richesses'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
