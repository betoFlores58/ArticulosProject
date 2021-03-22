from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy


class ArticuloListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'Products'

class DepartamentoView(DetailView):
    model = Post
    template_name = "articulos.html"
    context_object_name = 'Products'

class notaCreateView(CreateView):
    model = Post
    template_name = "notaNueva.html"
    fields = '__all__'

class notaUpdateView(UpdateView):
    model = Post
    template_name = "editarProducto.html"
    fields = ['nombre','precio','descripcion','imagen']

class notaDeleteView(DeleteView):
    model = Post
    template_name = "eliminarProducto.html"
    context_object_name = 'Products'
    success_url = reverse_lazy('home')
