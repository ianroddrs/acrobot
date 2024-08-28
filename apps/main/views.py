from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Bop
from django.db.models import Q

def home(request):
    return render(request,'home.html', {})

def resultado(request):

    print(request.POST.get('data'))
    data = json.loads(request.POST.get('data'))


    bop_query = Q()
    for chave, valor in data['boletim'].items():
        if chave == 'dataFato' and valor:
            bop_query &= Q(data_fato__date=valor) 
        if chave == 'dataRegistro' and valor:
            bop_query &= Q(data_registro__date=valor)
        if chave == 'registro' and valor:
            bop_query &= Q(registro__ds_registro=valor)
        if chave == 'relato' and valor:
            bop_query &= Q(relato__icontains=valor)

    pessoas_query = Q()
    for pessoa in data['pessoas']:
        pass

    
        # vestimenta_query = Q(bop_vestimenta__vestimenta__ds_vestimenta=pessoa['vestimenta']['tipo']) & Q(bop_vestimenta__cor__ds_cor=pessoa['vestimenta']['cor']) & Q(bop_vestimenta__estampa__ds_estampa_vestimenta=pessoa['vestimenta']['estampa'])    #     cabelo_query = Q(bop_cabelo__tipo_cabelo__ds_tipo_cabelo=pessoa['caracteristicasSomaticas']['cabelo']['tipo']) & Q(bop_cabelo__cor_cabelo__ds_cor_cabelo=pessoa['caracteristicasSomaticas']['cabelo']['cor']) & Q(bop_cabelo__comprimento_cabelo__ds_comprimento_cabelo=pessoa['caracteristicasSomaticas']['cabelo']['comprimento'])
        # tatuagem_query = Q(bop_tatuagem__local_tatuagem__ds_local_tatuagem=pessoa['tatuagem']['local'])
        # cabelo_query = Q(bop_cabelo__tipo_cabelo__ds_tipo_cabelo=pessoa['caracteristicasSomaticas']['cabelo']['tipo']) & Q(bop_cabelo__cor_cabelo__ds_cor_cabelo=pessoa['caracteristicasSomaticas']['cabelo']['cor']) & Q(bop_cabelo__comprimento_cabelo__ds_comprimento_cabelo=pessoa['caracteristicasSomaticas']['cabelo']['comprimento'])
        # pessoas_query |= (vestimenta_query & tatuagem_query & cabelo_query)

    veiculos_query = Q()
    # for veiculo in data['veiculos']:
    #     veiculos_query |= Q(bop_veiculo__veiculo__ds_modelo_veiculo=veiculo['modelo']) & Q(bop_veiculo__veiculo__marca_veiculo__ds_marca_veiculo=veiculo['marca']) & Q(bop_veiculo__cor__ds_cor=veiculo['cor']) & Q(bop_veiculo__placa_veiculo__ds_placa_veiculo=veiculo['placa'])

    localidades_query = Q()
    # for localidade in data['localidades']:
    #     localidades_query |= Q(bop__municipio__ds_municipio=localidade['municipio']) & Q(bop__distrito__ds_distrito_povoado=localidade['distrito']) & Q(bop__bairro__ds_bairro=localidade['bairro']) & Q(bop__aisp__ds_aisp=localidade['aisp']) & Q(bop__risp__ds_risp=localidade['risp'])

    # Combina as consultas
    query = bop_query & pessoas_query & veiculos_query & localidades_query

    # Executar a consulta
    bops = Bop.objects.filter(query)

    return JsonResponse(list(bops.values()), safe=False)