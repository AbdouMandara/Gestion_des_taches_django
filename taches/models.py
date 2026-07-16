from django.db import models

# Create your models here.
class Projet(models.Model) :
    nom = models.CharField(max_length=150, unique=True, blank=False)
    description_projet = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(db_comment="Date et periode que le projet a été créé", auto_now_add=True)

    