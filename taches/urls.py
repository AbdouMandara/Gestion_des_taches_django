from django.urls import path
from . import views
urlpatterns = [
    path('', views.liste_des_projets, name="Affichage_des_projets")
]