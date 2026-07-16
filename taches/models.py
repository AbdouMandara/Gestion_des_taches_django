from django.db import models

# Create your models here.
class Projet(models.Model) :
    nom = models.CharField(max_length=150, unique=True, blank=False)
    description_projet = models.TextField(blank=True) #retrait de null=TRUE car c'est bien pour les champs autre que TextField et CharField et null=TRUE va créer un pb  
    date_creation = models.DateTimeField(db_comment="Date et periode que le projet a été créé", auto_now_add=True)
    date_modification = models.DateTimeField(db_comment="Date de modif du projet", auto_now=True)
    
    class Meta : 
        ordering = ["date_creation"] # Permet de trier les projets par date de création dans l'ordre croissant
        verbose_name = "Projet" # Permet de changer le nom du modèle dans l'admin
        verbose_name_plural = "Projets" # Permet de changer le nom du modèle dans l'admin quand il y a plusieurs instances de ce modèle

    # Toujours faire ça car bonne pratique au niveau dashboard admin
    def __str__(self) -> str:
        return f"{self.nom}"

class Task(models.Model) :
    class STATUT(models.TextChoices) :
        """
        Classe qui enumère les valeurs qu'aura le statut d'une tache
        """
        EN_COURS = 'En cours'
        TERMINE = 'Terminé'
    
    class PRIORITE(models.TextChoices) :
        """
        Classe qui enumere les valeurs qu'aura la priorite d'une tache
        """
        HAUTE = 'Haute'
        BONNE = 'Bonne'
        FAIBLE = 'Faible'
    

    titre = models.CharField(unique=True, max_length=55)
    description_tache = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT, default=STATUT.EN_COURS)
    priorite = models.CharField(max_length=20, choices=PRIORITE, default=PRIORITE.BONNE)
    date_creation_tache = models.DateTimeField(db_comment="Date et periode que la tache a été créé", auto_now_add=True)
    date_modification_tache = models.DateTimeField(db_comment="Date de modif de la tache", auto_now=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)

    class Meta :
        ordering = ["titre"]
        verbose_name = "Tache"
        verbose_name_plural = "Taches"

    def __str__(self):
        return f"{self.titre}" 
    