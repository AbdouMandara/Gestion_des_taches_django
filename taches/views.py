from django.shortcuts import render, redirect, get_object_or_404
from .models import Projet
from .forms import ProjetForm
from django.contrib import messages

# Create your views here.

def liste_des_projets(request) :
    projets = Projet.objects.all()
    return render(request, 'templates_projets/list_projets.html',{'projets' : projets})

def creation_projet(request) :
    if request.method == 'POST' :
        form = ProjetForm(request.POST)
        if form.is_valid() :
            form.save()
            form = ProjetForm()
            messages.success(request, 'Projet créé avec succès !')
            return redirect('Affichage_des_projets')
        else :
            messages.error(request, 'Erreur lors de la création du projet')
    else :
            form = ProjetForm()
    return render(request,'templates_projets/create_projets.html', {'form' : form} )


def modification_projet(request, projet_id) :
    obj = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST' :
        form = ProjetForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = ProjetForm()
            messages.success(request, 'Projet mis à jour avec succès !')
            return redirect('Affichage_des_projets')
        else :
            messages.error(request, 'Erreur lors de la mise à jour du projet')
    else :
            form = ProjetForm(instance=obj)
    return render(request,'templates_projets/update_projets.html', {'form' : form} )

def suppression_projet(request, projet_id) :
    obj = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST' :
        obj.delete()
        messages.success(request, f'Produit : {obj.nom} supprimé avec succès !')
        return redirect('Affichage_des_projets')
    
    
    return render(request, 'templates_projets/delete_projets.html', {
        'name' : obj.nom,
    })