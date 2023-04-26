from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Categories(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    libelle = models.CharField(max_length=200)
    prix = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=5000)
    dateajout = models.DateTimeField(auto_now=True)
    categorie = ForeignKey(Categories, related_name='categorie', on_delete=models.CASCADE)

    class Trier:
        ordering = ['-dateajout']


class Client(models.Model):
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    telephone = models.IntegerField()


class Commande(models.Model):
    produit = ForeignKey(Produit, related_name='produit', on_delete=models.CASCADE)
    date = models.DateTimeField()
    mode_paiement = models.CharField(max_length=20)
    Client = ForeignKey(Client, related_name='client', on_delete=models.CASCADE)