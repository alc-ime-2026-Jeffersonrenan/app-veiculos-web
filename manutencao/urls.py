from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('veiculo/<int:pk>/', views.detalhes_veiculo, name='detalhes_veiculo'),
    path('servico/novo/', views.adicionar_servico, name='adicionar_servico'),
]
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('veiculo/<int:pk>/', views.detalhes_veiculo, name='detalhes_veiculo'),
    path('veiculo/novo/', views.adicionar_veiculo, name='adicionar_veiculo'),
    path('servico/novo/', views.adicionar_servico, name='adicionar_servico'),
]
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('veiculo/<int:pk>/', views.detalhes_veiculo, name='detalhes_veiculo'),
    path('veiculo/novo/', views.adicionar_veiculo, name='adicionar_veiculo'),
    path('veiculo/<int:pk>/editar/', views.editar_veiculo, name='editar_veiculo'),
    path('veiculo/<int:pk>/apagar/', views.apagar_veiculo, name='apagar_veiculo'),
    path('servico/novo/', views.adicionar_servico, name='adicionar_servico'),
]