import csv
from django.core.management import BaseCommand
from memoized import memoized
from datetime import datetime
from django.db import transaction
import csv, io, requests, time
from tqdm import tqdm, trange
from multiprocessing.dummy import Pool
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


familybase = {'Cedrela fissilis': 'Meliaceae',
         'Annona dolabripetala': 'Annonaceae',
          'Lantana trifolia': 'Verbenaceae',
           'Maytenus aquifolia': 'Celastraceae',
            'Anthurium pentaphyllum': 'Araceae',
             'Solanum americanum': 'Solanaceae',
              'Solanum lycocarpum': 'Solanaceae',
               'Inga edulis': 'Leguminosae',
                'Schizolobium paratyba': 'Leguminosae',
                 'Myrsine umbellata': 'Primulaceae',
                  'Annona sylvatica': 'Annonaceae',
                   'Alchornea sidifolia': 'Euphorbiaceae',
                    'Myrceugenia myrcioides': 'Myrtaceae',
                     'Senna multijuga': 'Leguminosae',
                      'Xylopia brasiliensis': 'Annonaceae',
                       'Prestonia coalita': 'Apocynaceae',
                        'Cabralea canjerana': 'Meliaceae',
                         'Sphagneticola trilobata': 'Compositae',
                          'Centella asiatica': 'Apiaceae',
                           'Justicia carnea': 'Acanthaceae',
                            'Guarea macrophylla': 'Meliaceae',
                             'Mimosa pudica': 'Leguminosae',
                              'Achyrocline alata': 'Compositae',
                               'Sida rhombifolia': 'Malvaceae',
                                'Solanum pseudoquina': 'Solanaceae',
                                 'Ocotea odorifera': 'Lauraceae',
                                  'Protium kleinii': 'Burseraceae',
                                   'Ludwigia octovalvis': 'Onagraceae',
                                    'Aspidosperma olivaceum': 'Apocynaceae',
                                     'Bactris setosa': 'Arecaceae',
                                      'Peltastes peltatus': 'Apocynaceae',
                                       'Psychotria vellosiana': 'Rubiaceae',
                                        'Piptadenia gonoacantha': 'Leguminosae',
                                         'Solanum castaneum': 'Solanaceae',
                                          'Jaegeria hirta': 'Compositae',
                                           'Guatteria australis': 'Annonaceae',
                                            'Asclepias curassavica': 'Apocynaceae',
                                             'Hedychium coronarium': 'Zingiberaceae',
                                              'Monstera adansonii': 'Araceae',
                                               'Baccharis semiserrata': 'Compositae',
                                                'Zanthoxylum rhoifolium': 'Rutaceae',
                                                 'Maprounea guianensis': 'Euphorbiaceae',
                                                  'Mikania micrantha': 'Compositae',
                                                   'Astrocaryum aculeatissimum': 'Arecaceae',
                                                    'Stachytarpheta cayennennsis': 'Verbenaceae',
                                                     'Solanum swartzianum': 'Solanaceae',
                                                      'Nectandra leucantha': 'Lauraceae',
                                                       'Piper gaudichaudianum': 'Piperaceae',
                                                        'Scoparia dulcis': 'Plantaginaceae',
                                                         'Casearia sylvestris': 'Salicaceae'}


@memoized
def findfamily(genus, species):
    address = f'http://www.theplantlist.org/tpl1.1/search?q={genus}%20{species}&csv=true'

    retry = 0
    erro = None
    while retry < 10:
        try:
            response = requests.get(
                address,
                timeout=10
            )
        except Exception as error:
            time.sleep(1)
            retry += 1
            erro = error
    else:
        print(f'Retry {retry} com error {erro}')
        print(address)
        raise Exception("Tentei familia demais")

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


def gerar_aliquota(especime):
    n_amostra = Amostra.objects.filter(
        amostra__id=especime.id
    ).first()

    if not n_amostra:
        n_amostra = Amostra()
        n_amostra.orgao = OrgaoDePlanta.objects.filter(orgao='Leaf').first()
        n_amostra.amostra = especime
        n_amostra.save()

    n_tipo_aliquota = obter_tipodealiquota()

    n_aliquota = Aliquota()
    n_aliquota.data = datetime.now()
    n_aliquota.tipo = n_tipo_aliquota
    n_aliquota.amostra = n_amostra
    n_aliquota.save()

    return n_aliquota


@memoized
def gerar_especie_aliquota(n_aliquota, algoritmo, database):
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



def processar_biodiversidade(aliquota, biodiversidade):
    sequenciamento = gerar_especie_aliquota(
                    aliquota,
                    'diamond',
                    'uniProt')

    incluir_sequencia(
                    sequenciamento,
                    biodiversidade
                )


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arquivo', nargs=1, type=str)
        parser.add_argument('especime', nargs=1, type=str)

    def handle(self, *args, **options):
        arquivo = options['arquivo'][0]
        especime = options['especime'][0]

        especime = Especime.objects.filter(
            identificador__startswith=especime
        ).first()

        aliquota = gerar_aliquota(especime)

        with open(arquivo, 'r') as marquivo:
            reader = csv.DictReader(
                marquivo,
                delimiter='\t'
            )

            for novo in tqdm(reader):
                novo.pop('id')
                novo.pop('sequenciamento_id')

                n_biodiversidade = Biodiversidade(
                    **novo
                )
                n_biodiversidade.geneid = n_biodiversidade.geneid[:199]

                processar_biodiversidade(aliquota, n_biodiversidade)
