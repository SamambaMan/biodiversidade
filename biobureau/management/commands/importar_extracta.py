from collections import defaultdict, OrderedDict
from memoized import memoized
from django.core.management import BaseCommand
from django.db import connection
from django.utils.timezone import localtime
from biobureau.models import (
    Familia,
    Genero,
    Especie,
    Especime,
    OrgaoDePlanta,
    Amostra,
    Aliquota,
    Fracionamento,
    TipoDeFracionamento,
    TipoDeAliquota,
    Fracao,
    Composto,
    DadosTLC,
    PlacaTLC,
    Eluente,
    ClasseQuimica
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
    DadosTLC.objects.all().delete()
    PlacaTLC.objects.all().delete()
    Composto.objects.all().delete()
    Fracao.objects.all().delete()
    Fracionamento.objects.all().delete()
    Aliquota.objects.all().delete()
    Fracionamento.objects.all().delete()
    Aliquota.objects.all().delete()
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
_FRACIONAMENTOS = "select * from fractionation where pfssampleid = #"
_SAMPLE = "select * from sample where sampleid = #"
_FRACOES = "select * from fraction where fractionationid = #"
_COMPOSTOS = "select * from compound where sampleid = #"
_TLCDATA = "select * from tlcdata where sampleid = #"
_TLCPLACA = "select * from tlcplate where tlcplateid = #"
_CLASSE_QUIMICA = "select * from chemical_classes where chemclassid = #"

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


@memoized
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

        importar_fracionamentos(n_amostra, orgao['sampleid'], cursor)

@memoized
def obter_tipo_fracionamento(nome):
    fracionamento = TipoDeFracionamento.objects.filter(nome=nome).first()
    if fracionamento:
        return fracionamento
    fracionamento = TipoDeFracionamento()
    fracionamento.nome = nome
    fracionamento.save()
    return fracionamento

@memoized
def obter_tipo_de_aliquota():
    tipo = TipoDeAliquota.objects.all().first()
    if tipo:
        return tipo
    tipo = TipoDeAliquota()
    tipo.nome = "Fracionamento"
    tipo.save()
    return tipo

def importar_fracionamentos(orgao, sampleid, cursor):
    cursor.execute(_SAMPLE.replace(
        "#",
        str(sampleid)
    ))
    sample = dictfetchall(cursor)[0]
    tipo_fracionamento = obter_tipo_fracionamento(sample['type'])

    cursor.execute(_FRACIONAMENTOS.replace(
        "#",
        str(sampleid)
    ))
    fracionamentos = dictfetchall(cursor)
    for fracionamento in fracionamentos:
        print(f"Importando fracionamento {fracionamento['fractionationid']}")
        n_aliquota = Aliquota()
        n_aliquota.tipo = obter_tipo_de_aliquota()
        n_aliquota.data = datetime.now()
        n_aliquota.amostra = orgao
        n_aliquota.save()

        n_fracionamento = Fracionamento()
        n_fracionamento.aliquota = n_aliquota
        n_fracionamento.tipo_de_fracionamento = tipo_fracionamento
        n_fracionamento.protocolo = fracionamento['frac_protocol']
        n_fracionamento.save()

        importar_tlc(
            None,
            fracionamento['pfssampleid'],
            cursor,
            n_fracionamento
        )


        importar_fracoes(
            n_fracionamento,
            fracionamento['fractionationid'],
            cursor
        )

def importar_fracoes(fracionamento, fractionationid, cursor):
    cursor.execute(_FRACOES.replace(
        "#",
        str(fractionationid)
    ))
    fracoes = dictfetchall(cursor)
    for fracao in fracoes:
        print(f"Importando fracao sample {fracao['sampleid']}")
        n_fracao = Fracao()
        n_fracao.fracionamento = fracionamento
        n_fracao.rt_inicial = fracao['rt_start']
        n_fracao.rt_final = fracao['rt_end']
        n_fracao.numero_fracao = fracao['frac_number']
        n_fracao.notas = fracao['notes']
        n_fracao.save()

        importar_compostos(n_fracao, fracao['sampleid'], cursor)
        importar_tlc(n_fracao, fracao['sampleid'], cursor)

def importar_tlc(fracao, sampleid, cursor, fracionamento=None):
    cursor.execute(_TLCDATA.replace(
        "#",
        str(sampleid)
    ))
    tlcdatas = dictfetchall(cursor)
    for tlcdata in tlcdatas:
        print(f"Importando TLCDATA sample {sampleid} ")
        placa = importar_placa_tlc(tlcdata['tlcplateid'], cursor)
        classe = importar_classe_quimica(tlcdata['chemclassid'], cursor)
        n_tlc = DadosTLC()
        n_tlc.fracao = fracao
        n_tlc.fracionamento = fracionamento
        n_tlc.placa = placa
        n_tlc.classe_quimica = classe
        n_tlc.quantidade = tlcdata['quantity']
        n_tlc.linha = tlcdata['lane']
        n_tlc.coluna = tlcdata['col']
        n_tlc.resultado = tlcdata['result']
        n_tlc.save()


@memoized
def importar_classe_quimica(idclasse, cursor):
    if not idclasse:
        return None
    cursor.execute(_CLASSE_QUIMICA.replace(
        "#",
        str(idclasse)
    ))
    classes = dictfetchall(cursor)
    for classe in classes:
        nome = classe['classname']
        existente = ClasseQuimica.objects.filter(nome=nome).first()
        if existente:
            return existente
        n_classe = ClasseQuimica()
        n_classe.nome = nome
        n_classe.save()
        return n_classe


@memoized
def importar_placa_tlc(idplaca, cursor):
    n_placa = PlacaTLC.objects.filter(idextracta=idplaca).first()
    if n_placa:
        return n_placa

    cursor.execute(_TLCPLACA.replace(
        "#",
        str(idplaca)
    ))
    placas = dictfetchall(cursor)
    for placa in placas:
        print(f"Importando placa TLC id {idplaca} ")
        n_placa = PlacaTLC()
        n_placa.numero_de_faixas = placa['nlanes']
        n_placa.data_da_analise = placa['analdate']
        n_placa.eluente = Eluente.objects.get(pk=placa['eluent_developer']) if placa['eluent_developer'] else None
        n_placa.notas = placa['notes']
        n_placa.idextracta = idplaca
        n_placa.save()
        return n_placa


def importar_compostos(fracao, sampleid, cursor):
    cursor.execute(_COMPOSTOS.replace(
        "#",
        str(sampleid)
    ))
    compostos = dictfetchall(cursor)
    for composto in compostos:
        print(f"Importando Composto")
        n_composto = Composto()
        n_composto.fracao = fracao
        n_composto.data_isolamento = composto['isolationdate']
        n_composto.depid = composto['depid']
        n_composto.notas = composto['notas']
        n_composto.percentual_de_pureza = composto['purity_pct']
        n_composto.notas_sobre_pureza = composto['purity_notes']
        n_composto.quantidade = composto['quantity']
        n_composto.volume = composto['volume']
        n_composto.solvente = composto['solvent']
        n_composto.mw = composto['mw']
        n_composto.formula = composto['formula']
        n_composto.nome_IUPAC = composto['name_iupac']
        n_composto.smiles = composto['smiles']
        n_composto.save()


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
