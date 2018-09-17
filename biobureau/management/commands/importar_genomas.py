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
    Sequencia
)
from listagens.models import (
    Biodiversidade
)

@memoized
def findfamily(genus, species):

    print(f"Planteando {genus} {species}")
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


def limpabanco():
    pass

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Contando biodiversidades')
        nbio = 100 # Biodiversidade.objects.all().count()
        print('Começando a brincadeira')
        for i in tqdmrange(nbio):
            biodiversidade = Biodiversidade.objects.all()[i]

            genero, especie = biodiversidade.species.split()
            sequenciamento = gerar_especie_aliquota(
                genero,
                especie,
                biodiversidade.algorithm,
                biodiversidade.database)
            



