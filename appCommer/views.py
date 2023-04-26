from django.shortcuts import render
from .models import Produit

# Create your views here.


def index(request):
    articles = Produit.objects.all()
    template_name = 'index.html'
    return render(request, template_name, {
        'articles': articles
    })