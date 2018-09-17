from django.core.management import BaseCommand
from memoized import memoized
from datetime import datetime
import csv, io, requests
from tqdm import tqdm
from biobureau.models import (
    Familia,
    Genero,
    Especie,
    Amostra,
    Aliquota,
    TipoDeAliquota,
    OrgaoDePlanta,
    Especime,
    Algoritmo,
    Database,
    Sequenciamento,
    Sequencia,
    GeneInfo,
    GeneOntology
)
from listagens.models import (
    Biodiversidade
)

@memoized
def findfamily(genus, species):
    address = f'http://www.theplantlist.org/tpl1.1/search?q={genus}%20{species}&csv=true'

    response = requests.get(
        address,
        timeout=10
    )

    reader = csv.DictReader(
        io.StringIO(
            response.content.decode('utf-8')
        )
    )

    for read in reader:
        return read['Family']

    raise Exception("Family not found")


@memoized
def obter_tipodealiquota():
    n_tipo_aliquota = TipoDeAliquota.objects.filter(nome="Sequenciamento").first()

    if not n_tipo_aliquota:
        n_tipo_aliquota = TipoDeAliquota()
        n_tipo_aliquota.nome = "Sequenciamento"
        n_tipo_aliquota.save()
    return n_tipo_aliquota 


@memoized
def obter_algoritmo(algoritmo):
    n_algoritmo = Algoritmo.objects.filter(nome=algoritmo).first()

    if not n_algoritmo:
        n_algoritmo = Algoritmo()
        n_algoritmo.nome = algoritmo
        n_algoritmo.save()
    
    return n_algoritmo


@memoized
def obter_database(database):
    n_database = Database.objects.filter(nome=database).first()

    if not n_database:
        n_database = Database()
        n_database.nome = database
        n_database.save()

    return n_database


@memoized
def gerar_especie_aliquota(genero, especie, algoritmo, database):
    familia = findfamily(genero, especie)

    n_especie = obter_especie(familia, genero, especie)

    n_especime = Especime.objects.filter(
        especie__id=n_especie.id
    ).first()

    if not n_especime:
        n_especime = Especime()
        n_especime.especie = n_especie
        n_especime.save()

    n_amostra = Amostra.objects.filter(
        amostra__id=n_especime.id
    ).first()

    if not n_amostra:
        n_amostra = Amostra()
        n_amostra.orgao = OrgaoDePlanta.objects.filter(orgao='Leaf').first()
        n_amostra.amostra = n_especime
        n_amostra.save()
    
    n_tipo_aliquota = obter_tipodealiquota()

    n_aliquota = Aliquota.objects.filter(
        tipo__id=n_tipo_aliquota.id,
        amostra__id=n_amostra.id
    ).first()

    if not n_aliquota:
        n_aliquota = Aliquota()
        n_aliquota.data = datetime.now()
        n_aliquota.tipo = n_tipo_aliquota
        n_aliquota.amostra = n_amostra
        n_aliquota.save()
    
    n_algoritmo = obter_algoritmo(algoritmo)
    n_database = obter_database(database)

    n_sequenciamento = Sequenciamento.objects.filter(
        aliquota__id=n_aliquota.id,
        algoritmo=n_algoritmo,
        database=n_database
    ).first()

    if not n_sequenciamento:
        n_sequenciamento = Sequenciamento()
        n_sequenciamento.data = datetime.now()
        n_sequenciamento.database = n_database
        n_sequenciamento.algoritmo = n_algoritmo
        n_sequenciamento.aliquota = n_aliquota
        n_sequenciamento.save()
    
    return n_sequenciamento


@memoized
def obter_especie(familia, genero, especie):
    n_familia = Familia.objects.filter(nome=familia).first()

    if not n_familia:
        n_familia = Familia()
        n_familia.nome = familia
        n_familia.save()
    
    n_genero = Genero.objects.filter(
        nome=genero,
        familia__id=n_familia.id
    ).first()

    if not n_genero:
        n_genero = Genero()
        n_genero.nome = genero
        n_genero.familia = n_familia
        n_genero.save()
    
    n_especie = Especie.objects.filter(
        nome=especie,
        genero__id=n_genero.id
    ).first()

    if not n_especie:
        n_especie = Especie()
        n_especie.genero = n_genero
        n_especie.nome = especie
        n_especie.save()
    
    return n_especie


@memoized
def obter_gi(gi):
    gi = int(gi)
    n_gi = GeneInfo.objects.filter(
        identificacao=gi
    ).first()

    if not n_gi:
        n_gi = GeneInfo()
        n_gi.identificacao = gi
        n_gi.save()

    return n_gi


@memoized
def obter_gis(stringgi):
    gis = stringgi.split(';')
    gis = [x.strip() for x in gis]
    return [obter_gi(gi) for gi in gis]


@memoized
def obter_go(go):
    n_go = GeneOntology.objects.filter(
        nome = go
    ).first()

    if not n_go:
        n_go = GeneOntology()
        n_go.nome = go
        n_go.save()
    
    return n_go


@memoized
def obter_gos(stringgo):
    gos = stringgo.split()
    gos = [x.strip() for x in gos]
    return [obter_go(go) for go in gos]


def limpabanco():
    Sequencia.objects.all().delete()


def incluir_sequencia(sequenciamento, biodiversidade):
    n_sequencia = Sequencia()
    n_sequencia.sequenciamento = sequenciamento
    n_sequencia.qseqid = biodiversidade.qseqid
    n_sequencia.sseqid = biodiversidade.sseqid
    n_sequencia.pident = biodiversidade.pident
    n_sequencia.length = biodiversidade.length
    n_sequencia.mismatch = biodiversidade.mismatch
    n_sequencia.gapopen = biodiversidade.gapopen
    n_sequencia.qstart = biodiversidade.qstart
    n_sequencia.qend = biodiversidade.qend
    n_sequencia.sstart = biodiversidade.sstart
    n_sequencia.send = biodiversidade.send
    n_sequencia.evalue = biodiversidade.evalue
    n_sequencia.bitscore = biodiversidade.bitscore
    n_sequencia.geneid = biodiversidade.geneid
    n_sequencia.ncbitaxon = biodiversidade.ncbitaxon
    n_sequencia.ltaxon = biodiversidade.ltaxon
    n_sequencia.repid = biodiversidade.repid
    n_sequencia.clustername = biodiversidade.clustername
    n_sequencia.station = biodiversidade.station
    n_sequencia.save()

    if biodiversidade.gi and biodiversidade.gi.strip():
        n_sequencia.geneinfo.add(
            *obter_gis(
                biodiversidade.gi
            )
        )

    if biodiversidade.obs and biodiversidade.obs.strip():
        n_sequencia.geneontology.add(
            *obter_gos(
                biodiversidade.obs
            )
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        limpabanco()
        print('Contando biodiversidades')
        items = Biodiversidade.objects.filter(algorithm='diamond')
        nbio = 100 # items.count()
        print('Começando a brincadeira')
        for i in tqdm(range(nbio)):
            biodiversidade = items[i]

            genero, especie = biodiversidade.species.split()
            sequenciamento = gerar_especie_aliquota(
                genero,
                especie,
                biodiversidade.algorithm,
                biodiversidade.database)
            
            incluir_sequencia(
                sequenciamento,
                biodiversidade
            )

