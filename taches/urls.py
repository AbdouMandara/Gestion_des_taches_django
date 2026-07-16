from django.urls import path
from . import views
urlpatterns = [
    path('', views.liste_des_projets, name="Affichage_des_projets"),
    path('creation', views.creation_projet, name='Creation_de_projet'),
    path('mise_a_jour/<int:projet_id>', views.modification_projet, name='Mise_a_jour_du_projet')
]