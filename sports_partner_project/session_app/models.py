from django.db import models

# Create your models here.

class Selection(models.Model):
    nbre_person_a = models.IntegerField(default=0)
    nbre_person_z = models.IntegerField(default=0)
    lieu = models.CharField(max_length=30)
    niveau = models.IntegerField(default=0)
    age_search = models.IntegerField(default=0)

    def __str__(self):
        return self.lieu

    def __repr__(self):
        return "<Selection {}>".format(self.lieu)
