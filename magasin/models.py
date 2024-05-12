from django.db import models 
from datetime import date


class Categorie(models.Model): 
    Type_CHOICES=[('AI','Alimentaire'),('Mb','Meuble'),('Sn','Sanitaire'),('Vs','Vaisselle'),
                  ('Vt','Vetement'),('Jx','Jouets'),('Lg','Ligne de Maison'),('Bj','Bijoux'),('Dc','Decor')]
    name=models.CharField(max_length=50,choices=Type_CHOICES,default='Al')
    def __str__(self) :
        return self.name 
    
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8) 
    def __str__(self) :
        return self.nom+""+self.adresse+" "+self.email+""+self.telephone    


class Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballe')]
    libelle=models.CharField(max_length=100)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE ,null=True)
    fornisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return  self.libelle +" " + self.description + " "+ str(self.prix)+" "+ self.type 


class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField(Produit)
    def __str__(self) :
        return str(self.dateCde) +" "+str(self.totalCde) 
    def calculer_total (self):
        return sum(Produit.prix for Produit in self.produits.all())




class ProduitsNC(Produit):
    Dugree_garantie=models.CharField(max_length=100)
    def __str__(self) :
        return self.Dugree_garantie
    
# Create your models here.
        


