from django.contrib import admin
from .models import Projet, Task
# Register your models here.

@admin.register(Projet)
class Admin_Projet(admin.ModelAdmin) :
    list_display = ('nom', 'description_projet', 'date_creation', 'date_modification')

@admin.register(Task)
class Admin_Task(admin.ModelAdmin) :
    list_display = ('titre', 'description_tache', 'statut', 'priorite', 'date_creation_tache', 'date_modification_tache', 'projet')
    list_filter = ('statut', 'priorite', 'projet')
    search_fields = ('titre', 'description_tache')