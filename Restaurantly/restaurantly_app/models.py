# membres/models.py

from django.db import models

class Membre(models.Model):
    nom = models.CharField(max_length=40)
    age = models.IntegerField()
    genre = models.CharField(max_length=10)

    class Meta:
        db_table = 'membres'  # Nom de la table complet


