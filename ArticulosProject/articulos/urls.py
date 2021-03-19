from django.urls import path
from .views import ArticuloListView, DepartamentoView

urlpatterns = [
    path('nota/<int:pk>/', DepartamentoView.as_view(), name='articulos'),
    path('', ArticuloListView.as_view(), name='home')
]