from django.urls import path ,include
from . import views

from django.contrib.auth import views as auth_views
from .views import CategoryAPIView ,ProduitAPIView ,ProductViewset



urlpatterns = [
 path('', views.index, name='index'),
 path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
 path('nouvCmd/',views.nouveaucommende,name='nouveauCmd'),
 path('register/',views.register, name = 'register'),
 path('logout/',views.logout_view, name = 'logout'),
 path('api/category/', CategoryAPIView.as_view()) ,
 path('api/produit/', ProduitAPIView.as_view()),
 
]
