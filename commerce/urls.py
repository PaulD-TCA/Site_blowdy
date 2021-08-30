from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('commerce/', views.commerce, name='commerce'),
    path('commerce/livres/', views.livres, name='livres'),
    path('mug_ppme/', views.mug_ppme, name='mug_ppme'),
    path('Assiettes/', views.Assiettes, name='Assiettes'),
    path('Sacs/', views.Sacs, name='Sacs'),
    path('Valise_ppme/', views.Valise_ppme, name='Valise_ppme'),
    path('Couette_et_taie/', views.Couette_et_taie, name='Couette_et_taie'),
    path('Mug_GERATP/', views.Mug_GERATP, name='Mug_GERATP'),
    path('Sac_GERATP/', views.Sac_GERATP, name='Sac_GERATP'),
    path('Sweet/', views.Sweet, name='Sweet'),
    path('Tapis_souris_GERATP/', views.Tapis_souris_GERATP, name='Tapis_souris_GERATP'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
