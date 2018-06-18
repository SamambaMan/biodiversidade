from io import TextIOWrapper
import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from listagens.models import Biodiversidade


@csrf_exempt
def importacao(infile):
    saida = ""
    with open(infile, 'r') as linhas:
        conta = 0
        cabecalho = None
        for linha in linhas:
            detalhe = [x.strip() for x in linha.split('\t')]
            if not conta:
                cabecalho = detalhe
                conta += 1 
                continue
            conta += 1
    
            try:
                entrada = {}
                for chave, valor in zip(cabecalho, detalhe):
                    entrada[chave] = valor

                novo = Biodiversidade(**entrada)
            except:
                pass

            try:
                novo.save()
            except Exception as error:
                saida += str(conta) + " -- " + error.message + " -- " + linha 
                print(str(conta) + " -- " + error.message + " -- " + linha)

    return HttpResponse(saida)
