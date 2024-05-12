from django.urls import path
from accounts import views
from blog.views import CreerPost, DetailPost, ListePost, ModifierPost, SupprimerPost
urlpatterns = [
    path('', ListePost.as_view(), name='liste_posts'),
    path('<int:pk>/', DetailPost.as_view(),name='detail_post'),
    path('ajouter/', CreerPost.as_view(),name='creer_post'),
    path('<int:pk>/modifier/', ModifierPost.as_view(),name='modifier_post'),
    path('<int:pk>/supprimer/', SupprimerPost.as_view(),name='supprimer_post'),

]