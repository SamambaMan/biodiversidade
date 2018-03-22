from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def importacao(infile):
    from io import TextIOWrapper
    import csv
    from listagens.models import Biodiversidade

    saida = ""
    with open(infile, 'r') as linhas:
        conta = 0
        for linha in linhas:
            conta += 1
            detalhe = linha.split('\t')
            novo = Biodiversidade()

            try:
                novo.species = detalhe[0][:200]
                novo.algorithm = detalhe[1][:200]
                novo.database = detalhe[2][:200]
                novo.qseqid = detalhe[3][:200]
                novo.sseqid = detalhe[4][:200]
                novo.pident = detalhe[5][:200]
                novo.length = detalhe[6][:200]
                novo.mismatch = detalhe[7][:200]
                novo.gapopen = detalhe[8][:200]
                novo.qstart = detalhe[9][:200]
                novo.qend = detalhe[10][:200]
                novo.sstart = detalhe[11][:200]
                novo.send = detalhe[12][:200]
                novo.evalue = detalhe[13][:200]
                novo.bitscore = detalhe[14][:200]
                novo.gi = detalhe[15][:5000]
                novo.geneid = detalhe[16][:200]
                novo.ncbitaxon = detalhe[17][:200]
                novo.ltaxon = detalhe[18][:200]
                novo.repid = detalhe[19][:200]
                novo.clustername = detalhe[20][:500]
                novo.obs = detalhe[21][:1000]
            except:
                pass

            try:
                novo.save()
            except Exception, error:
                saida += str(conta) + " -- " + error.message + " -- " + linha 
                print str(conta) + " -- " + error.message + " -- " + linha 

    return HttpResponse(saida)
