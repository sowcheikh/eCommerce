from django.contrib import admin
from .models import Categories, Produit, Commande, Client


# Register your models here.


class GestionCategorie(admin.ModelAdmin):
    display = 'nom'


class GestionProduit(admin.ModelAdmin):
    list_display = ('libelle', 'prix', 'categorie', 'dateajout')


admin.site.register(Categories, GestionCategorie)
admin.site.register(Produit, GestionProduit)
admin.site.register(Client)
admin.site.register(Commande)
