from django.shortcuts import render
from .models import Projet
# Create your views here.

def liste_des_projets(request) :
    projets = Projet.objects.all()
    return render(request, 'templates_projets/list_projets.html',{'projets' : projets})
