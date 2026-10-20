from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import Veiculo, Servico
from .forms import ServicoForm, VeiculoForm

@login_required
def dashboard(request):
    veiculos_banco = Veiculo.objects.filter(usuario=request.user)
    veiculos = []
    hoje = date.today()
    
    total_frota = 0
    total_pecas = 0
    total_mao_obra = 0

    for v in veiculos_banco:
        servicos = v.servicos.all()
        ultimo_servico = servicos.order_by('-data_execucao').first()
        
        # Separa a soma por categoria para o gráfico
        for s in servicos:
            pecas = s.custo_pecas or 0
            mao_obra = s.custo_mao_obra or 0
            total_pecas += pecas
            total_mao_obra += mao_obra
            total_frota += (pecas + mao_obra)
        
        v.status_cor = "success"
        v.status_alerta = "EM DIA"
        v.status_mensagem = "Manutenção em dia"

        if ultimo_servico:
            atrasado = False
            a_vencer = False
            mensagens = []

            if ultimo_servico.periodicidade_meses:
                dias_validade = ultimo_servico.periodicidade_meses * 30
                data_vencimento = ultimo_servico.data_execucao + timedelta(days=dias_validade)
                
                if data_vencimento < hoje:
                    atrasado = True
                    mensagens.append(f"Venceu a {data_vencimento.strftime('%d/%m/%Y')}")
                elif data_vencimento <= hoje + timedelta(days=30):
                    a_vencer = True
                    mensagens.append(f"Vence a {data_vencimento.strftime('%d/%m/%Y')}")
                else:
                    mensagens.append(f"Até {data_vencimento.strftime('%d/%m/%Y')}")

            if ultimo_servico.quilometragem and ultimo_servico.periodicidade_km:
                km_limite = ultimo_servico.quilometragem + ultimo_servico.periodicidade_km
                mensagens.append(f"ou aos {km_limite} km")

            if atrasado:
                v.status_cor = "danger"
                v.status_alerta = "ATRASADO"
            elif a_vencer:
                v.status_cor = "warning text-dark"
                v.status_alerta = "A VENCER"
            
            if mensagens:
                v.status_mensagem = " ".join(mensagens)

        else:
            v.status_cor = "secondary"
            v.status_alerta = "SEM DADOS"
            v.status_mensagem = "Registe um serviço para iniciar alertas"

        veiculos.append(v)

    contexto = {
        'veiculos': veiculos,
        'total_frota': total_frota,
        'total_pecas': total_pecas,
        'total_mao_obra': total_mao_obra
    }
    return render(request, 'manutencao/dashboard.html', contexto)

@login_required
def detalhes_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk, usuario=request.user)
    servicos = veiculo.servicos.all().order_by('-data_execucao')
    total_gasto = sum(servico.custo_total for servico in servicos)
    
    contexto = {
        'veiculo': veiculo,
        'servicos': servicos,
        'total_gasto': total_gasto,
    }
    return render(request, 'manutencao/detalhes_veiculo.html', contexto)

@login_required
def adicionar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save()
            return redirect('detalhes_veiculo', pk=servico.veiculo.pk)
    else:
        form = ServicoForm()
        form.fields['veiculo'].queryset = Veiculo.objects.filter(usuario=request.user)
    
    return render(request, 'manutencao/adicionar_servico.html', {'form': form})

@login_required
def adicionar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            veiculo = form.save(commit=False)
            veiculo.usuario = request.user
            veiculo.save()
            return redirect('dashboard')
    else:
        form = VeiculoForm()
    
    return render(request, 'manutencao/adicionar_veiculo.html', {'form': form})

@login_required
def editar_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('detalhes_veiculo', pk=veiculo.pk)
    else:
        form = VeiculoForm(instance=veiculo)
    
    return render(request, 'manutencao/adicionar_veiculo.html', {'form': form, 'editando': True})

@login_required
def apagar_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        veiculo.delete()
        return redirect('dashboard')
        
    return render(request, 'manutencao/confirmar_apagar.html', {'veiculo': veiculo})