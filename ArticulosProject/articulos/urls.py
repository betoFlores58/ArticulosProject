from django.urls import path
from .views import ArticuloListView, DepartamentoView, notaCreateView,notaUpdateView,notaDeleteView

urlpatterns = [
    path('nota/<int:pk>/', DepartamentoView.as_view(), name='articulos'),
    path('', ArticuloListView.as_view(), name='home'),
    path('nota/Nueva', notaCreateView.as_view(), name='notaNueva'),
    path('nota/<int:pk>/editar', notaUpdateView.as_view(), name='editarProducto'),
    path('nota/<int:pk>/delete', notaDeleteView.as_view(), name='eliminarProducto'),
]