from django.shortcuts import render
from django.db import connection
from collections import defaultdict, OrderedDict
import csv
import random

_QUERY_STATUS_POR_CATEGORIA = """
select chm.classname, count(*)
from sample smp
inner join tlcdata tlc on 
    tlc.sampleid = smp.sampleid
inner join chemical_classes chm on
    chm.chemclassid = tlc.chemclassid
where smp.type = 'extract'
group by chm.classname
"""

_QUERY_STATUS_POR_ESPECIE = """
select tpl.family, tpl.genus, tpl.species, count(*)
from sample smp
inner join tplantorgan plo on
 plo.sampleid = smp.sampleid
inner join tplant tpl on 
 tpl.tplantid = plo.tplantid
inner join tlcdata tlc on
	tlc.sampleid = smp.sampleid
where subtype = 'tplant'
and type = 'extract'
group by tpl.family, tpl.genus, tpl.species
order by count(*) desc
"""

_QUERY_FRACOES_POR_EXTRATO_POR_PLANTA = """
select tpl.family, tpl.genus, tpl.species, count(1)
from sample smp_fr
inner join fraction frc on
   frc.sampleid = smp_fr.sampleid
inner join fractionation frn on
   frn.fractionationid = frc.fractionationid
inner join sample smp_ex on
   smp_ex.sampleid = frn.pfssampleid
inner join tplantorgan tpo on
   tpo.sampleid = smp_ex.sampleid
inner join tplant tpl on
   tpl.tplantid = tpo.tplantid
inner join tlcdata tlc on
   tlc.sampleid = smp_ex.sampleid
inner join tlcplate tlp on
	tlp.tlcplateid = tlc.tlcplateid
inner join chemical_classes chc on
   chc.chemclassid = tlc.chemclassid
where smp_fr.type = 'fraction'
%s
group by tpl.family, tpl.genus, tpl.species
order by count(1) desc	
"""


_QUERY_NUMERO_FRACOES_POR_ORGAO = """
select tpo.organ, count(1)
from sample smp_fr
inner join fraction frc on
   frc.sampleid = smp_fr.sampleid
inner join fractionation frn on
   frn.fractionationid = frc.fractionationid
inner join sample smp_ex on
   smp_ex.sampleid = frn.pfssampleid
inner join tplantorgan tpo on
   tpo.sampleid = smp_ex.sampleid
inner join tplant tpl on
   tpl.tplantid = tpo.tplantid
inner join tlcdata tlc on
   tlc.sampleid = smp_ex.sampleid
inner join tlcplate tlp on
	tlp.tlcplateid = tlc.tlcplateid
inner join chemical_classes chc on
   chc.chemclassid = tlc.chemclassid
where smp_fr.type = 'fraction'
%s
group by tpo.organ
order by count(1) desc
"""

_ELUENTE_INICIAL = "and tlp.eluent_developer <=3 "
_ELUENTE_FINAL = "and tlp.eluent_developer > 3 "


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        OrderedDict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def serializa(listagem):
    saida = []
    for item in listagem:
        linha = []
        for chave in item:
            linha.append(item[chave])
        saida.append(linha)
    return saida


def listagens():
    with connection.cursor() as cursor:
        cursor.execute(_QUERY_STATUS_POR_CATEGORIA)
        status_por_classe_quimica = dictfetchall(cursor)

        cursor.execute(_QUERY_STATUS_POR_ESPECIE)
        status_por_especie = dictfetchall(cursor)

        cursor.execute(_QUERY_FRACOES_POR_EXTRATO_POR_PLANTA % _ELUENTE_INICIAL)
        extrato_por_fracao_por_planta_inicial = dictfetchall(cursor)

        cursor.execute(_QUERY_FRACOES_POR_EXTRATO_POR_PLANTA % _ELUENTE_FINAL)
        extrato_por_fracao_por_planta_final = dictfetchall(cursor)

        cursor.execute(_QUERY_NUMERO_FRACOES_POR_ORGAO % _ELUENTE_INICIAL)
        extrato_por_orgao_inicial = dictfetchall(cursor)

        cursor.execute(_QUERY_NUMERO_FRACOES_POR_ORGAO % _ELUENTE_FINAL)
        extrato_por_orgao_final = dictfetchall(cursor)
        return {
            'status_por_classe_quimica': status_por_classe_quimica,
            'status_por_especie': status_por_especie,
            'extrato_por_fracao_por_planta_inicial': extrato_por_fracao_por_planta_inicial,
            'extrato_por_fracao_por_planta_final': extrato_por_fracao_por_planta_final,
            'extrato_por_orgao_inicial': extrato_por_orgao_inicial,
            'extrato_por_orgao_final': extrato_por_orgao_final
        }


def index(request):
    
    retorno = listagens()

    return render(
        request,
        'dashboard/index.html',
        retorno
    )
