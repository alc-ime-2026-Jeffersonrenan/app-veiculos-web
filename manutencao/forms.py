from django import forms
from .models import Servico, Veiculo

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = [
            'veiculo', 'data_execucao', 'tipo_servico', 'descricao', 
            'quilometragem', 'periodicidade_meses', 'periodicidade_km', 
            'custo_pecas', 'custo_mao_obra'
        ]
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'data_execucao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tipo_servico': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Troca de óleo e filtro'}),
            'quilometragem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 45000'}),
            'periodicidade_meses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 6'}),
            'periodicidade_km': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 10000'}),
            'custo_pecas': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'custo_mao_obra': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'placa', 'tipo']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Toyota'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Hilux'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2022'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: ABC-1234'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
        }