from collections import defaultdict, OrderedDict
from django.core.management import BaseCommand
from django.db import connection
from django.utils.timezone import localtime
from biobureau.models import (
    Familia,
    Genero,
    Especie,
    Especime,
    OrgaoDePlanta,
    Amostra
)
from datetime import datetime

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        OrderedDict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def limpabanco():
    Amostra.objects.all().delete()
    OrgaoDePlanta.objects.all().delete()
    Especime.objects.all().delete()
    Especie.objects.all().delete()
    Genero.objects.all().delete()
    Familia.objects.all().delete()
    

_FAMILIAS = "select distinct(family) from tplant"
_GENEROS = "select distinct(genus) from tplant where family #"
_ESPECIES = "select distinct(species) from tplant where genus # and family $"
_PLANTAS = "select * from tplant where species # and genus $ and family @"
_ORGAOS = "select * from tplantorgan where tplantid = #"


def compara_sql(entrada):
    return (f" = '{entrada}'" if entrada  else " is null")

def branco(entrada):
    return entrada if entrada else "Branco"

def importar_plantas(familia, genero, especie, n_especie, cursor):
    cursor.execute(
        _PLANTAS.replace(
            "#",
            compara_sql(especie)
       ).replace(
           "$",
           compara_sql(genero)
       ).replace(
           "@",
           compara_sql(familia)
       )
    )
    plantas = dictfetchall(cursor)
    for planta in plantas:
        n_especime = Especime()
        n_especime.especie = n_especie
        n_especime.data_da_coleta = planta['coldate']
        n_especime.altitude = planta['altitude']
        n_especime.solo = planta['soil']
        n_especime.vegetacao = planta['vegetation']
        n_especime.ponto_de_referencia = planta['mapinfo']
        n_especime.vegetacao = planta['vegetation']
        n_especime.nome_comum = planta['common']
        n_especime.autor = planta['author']
        n_especime.ligth = planta['light']
        n_especime.abund = planta['abund']
        n_especime.altura = planta['height']
        n_especime.diametro = planta['diameter']
        n_especime.habit = planta['habit']
        n_especime.photonum = planta['photonum']
        n_especime.numero_individuos = planta['numindiv']
        n_especime.etnologico = planta['ethnologic']
        n_especime.notas = planta['notes']
        n_especime.identid = planta['identid']
        n_especime.nome_erva = planta['herbname']
        n_especime.data_erva = planta['herbdate']
        n_especime.lat = planta['lat']
        n_especime.lng = planta['lon']
        n_especime.save()

        importar_orgaos_planta(n_especime, planta['tplantid'], cursor)


def obter_tipo_orgao(nome):
    orgao = OrgaoDePlanta.objects.filter(orgao=nome).first()
    if orgao:
        print(f"Retornando {orgao}")
        return orgao
    orgao = OrgaoDePlanta()
    orgao.orgao = nome
    orgao.save()
    print(f"Criando {orgao}")
    return orgao



def importar_orgaos_planta(planta, idplanta, cursor):
    cursor.execute(_ORGAOS.replace(
        "#",
       str(idplanta))
    )
    orgaos = dictfetchall(cursor)
    for orgao in orgaos:
        n_amostra = Amostra()
        tipo_orgao = obter_tipo_orgao(orgao['organ'])
        n_amostra.orgao = tipo_orgao
        n_amostra.amostra = planta
        n_amostra.cheiro = orgao['smell']
        n_amostra.cor = orgao['color']
        n_amostra.peso = orgao['weight']
        n_amostra.notas = orgao['notes']

        n_amostra.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        limpabanco()
        with connection.cursor() as cursor:
            cursor.execute(_FAMILIAS)
            familias = dictfetchall(cursor)
            for familia in familias:
                print(f"Importando {familia['family']}")
                n_familia = Familia()
                n_familia.nome = branco(familia['family'])
                n_familia.save()
                cursor.execute(
                    _GENEROS.replace(
                        "#",
                        compara_sql(familia['family'])
                    )
                )
                generos = dictfetchall(cursor)
                for genero in generos:
                    print(f"Importando {genero['genus']}")
                    n_genero = Genero()
                    n_genero.familia = n_familia
                    n_genero.nome = branco(genero['genus'])
                    n_genero.save()

                    cursor.execute(
                        _ESPECIES.replace(
                            "#",
                            compara_sql(genero['genus'])
                        ).replace(
                            "$",
                            compara_sql(familia['family'])
                        )  
                    )
                    especies = dictfetchall(cursor)
                    for especie in especies:
                        print(f"Importando {especie['species']}")
                        n_especie = Especie()
                        n_especie.genero = n_genero
                        n_especie.nome = branco(especie['species'])
                        n_especie.save()

                        importar_plantas(
                            familia['family'],
                            genero['genus'],
                            especie['species'],
                            n_especie,
                            cursor
                        )
