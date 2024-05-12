from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.forms import PostForm

from .models import Post

class ListePost(ListView):
    model = Post
    template_name = 'mag/liste_posts.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'mag/detail_post.html'
    context_object_name = 'post'

class CreerPost(CreateView):
    model = Post
    template_name = 'mag/creer_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_posts')

class ModifierPost(UpdateView):
    model = Post
    template_name = 'mag/modifier_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_posts')

class SupprimerPost(DeleteView):
    model = Post
    template_name = 'mag/supprimer_post.html'
    success_url = reverse_lazy('liste_posts')
