from django.db import models
from django.contrib.auth.models import User # <-- 1. Adicione esta importação no topo

class Servico(models.Model):
    # Adicione esta linha exata à sua tabela de Serviços:
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
class Veiculo(models.Model):
    # 2. Adicione este campo à sua tabela de veículos:
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
class Veiculo(models.Model):
    TIPO_VEICULO = [
        ('CAR', 'Carro'),
        ('MOT', 'Moto'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='veiculos')
    tipo = models.CharField(max_length=3, choices=TIPO_VEICULO)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

class Servico(models.Model):
    TIPO_SERVICO = [
        ('PREV', 'Preventivo'),
        ('CORR', 'Corretivo'),
    ]
    
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='servicos')
    data_execucao = models.DateField()
    tipo_servico = models.CharField(max_length=4, choices=TIPO_SERVICO)
    descricao = models.CharField(max_length=200)
    quilometragem = models.IntegerField(help_text="KM no momento do serviço")
    
    periodicidade_meses = models.IntegerField(null=True, blank=True, help_text="Repetir em X meses")
    periodicidade_km = models.IntegerField(null=True, blank=True, help_text="Repetir em X km")
    
    custo_pecas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    custo_mao_obra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    @property
    def custo_total(self):
        return self.custo_pecas + self.custo_mao_obra

    def __str__(self):
        return f"{self.get_tipo_servico_display()} - {self.veiculo.modelo} em {self.data_execucao}"