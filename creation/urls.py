from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('creation/', views.creation, name='creation'),
    path('aura_chromatic/', views.aura_chromatic, name='aura_chromatic'),
    path('aura_chromatic_2/', views.aura_chromatic_2, name='aura_chromatic_2'),
    path('Debacle_polaire/', views.Debacle_polaire, name='Debacle_polaire'),
    path('Echos_d_ames/', views.Echos_d_ames, name='Echos_d_ames'),
    path('La_fleur_verte_de_Sylvie/', views.La_fleur_verte_de_Sylvie, name='La_fleur_verte_de_Sylvie'),
    path('L_ecrivain/', views.L_ecrivain, name='L_ecrivain'),
    path('Lex_o_Mille/', views.Lex_o_Mille, name='Lex_o_Mille'),
    path('L_inconstance/', views.L_inconstance, name='L_inconstance'),
    path('Lumiere_a_l_horizon/', views.Lumiere_a_l_horizon, name='Lumiere_a_l_horizon'),
    path('Old_vintage/', views.Old_vintage, name='Old_vintage'),
    path('Spirale/', views.Spirale, name='Spirale'),
    path('Stigmate_3/', views.Stigmate_3, name='Stigmate_3'),
    path('Symphonie_de_rue/', views.Symphonie_de_rue, name='Symphonie_de_rue'),
    path('Une_vie_representee/', views.Une_vie_representee, name='Une_vie_representee'),
    path('Vue_de_l_espace/', views.Vue_de_l_espace, name='Vue_de_l_espace'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
