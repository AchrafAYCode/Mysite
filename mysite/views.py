from django.shortcuts import render
from django.template import loader

from django.contrib.auth.decorators import login_required
@login_required

def index (request):
    context={'val':"Menu Acceuil"}
    return render(request,'magasin/acceuil.html',context)


