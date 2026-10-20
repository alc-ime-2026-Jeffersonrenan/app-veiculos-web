from django.contrib import admin
from .models import Veiculo, Servico

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    # Escolha as colunas que quer ver na tabela do painel
    list_display = ('id', 'usuario', 'placa', 'marca') 
    
    # Cria um menu lateral para filtrar resultados
    list_filter = ('usuario', 'marca') 
    
    # Adiciona uma barra de pesquisa
    search_fields = ('placa', 'marca', 'usuario__username')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'veiculo', 'tipo_servico', 'data_execucao', 'quilometragem')
    list_filter = ('usuario', 'tipo_servico', 'data_execucao')
    search_fields = ('veiculo__placa', 'descricao', 'usuario__username')