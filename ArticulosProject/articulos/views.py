from django.views.generic import ListView, DetailView
from .models import Post

class ArticuloListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'Products'

class DepartamentoView(DetailView):
    model = Post
    template_name = "articulos.html"
    context_object_name = 'Products'
