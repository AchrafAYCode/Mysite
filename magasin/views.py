from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from .models import Produit
from .models import Fournisseur
from .models import Commande
from django.template import loader
from .forms import ProduitForm 
from .forms import FournisseurForm
from .forms import CommandeForm
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def nouveaucommende(request) :
    if request.method =='POST' :
        form=CommandeForm(request.POST)
        if form.is_valid() :
            form.save()
    else :
        form=CommandeForm()
    
    commandes= Commande.objects.all()

    return render(request, 'magasin/Commande.html', {'form': form, 'commandes': commandes})


def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauFour')
    else:
        form = FournisseurForm()
    
    fournisseurs = Fournisseur.objects.all()
    
    return render(request, 'magasin/Fournisseur.html', {'form': form, 'fournisseurs': fournisseurs})






def index(request):
    #products= Produit.objects.all()
    #context={'products':products} 
    if(request.method=="POST") :
        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else : 
        form=ProduitForm()
    
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{ 'list':list})

    #return render( request,'magasin/majProduits.html',{'form':form})


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')
    return render(request, 'magasin/registration/register.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logoutt ( request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
   

def login(request) :
    
    if request .method=="POST" :
        form = AuthenticationForm(request .POST)
        if form . is_valid() :
            user_email = form.cleaned_data['email']
            logged_user = User.objects.get(courriel=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect ('/home')
        else:
            form = AuthenticationForm()
    return render('registration/login.html ' , {'form' : form}) 


def logout_view(request): logout(request) # Redirect to a success page.


from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie 
from magasin.serializers import CategorySerializer ,ProduitSerializer

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data) 

class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data) 
    
    
from rest_framework import viewsets
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset