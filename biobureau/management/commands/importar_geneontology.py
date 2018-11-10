import csv
from tqdm import tqdm
from django.core.management import BaseCommand
from memoized import memoized
from biobureau.models import GeneOntology
from multiprocessing.dummy import Pool

def importar(linha):
    if linha[4] not in todosgo:
        return None
    go = GeneOntology.objects.get(nome=linha[4])

    go.descricao = linha[9]
    go.save()

todosgo = {}

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arquivo', nargs=1, type=str)
    
    def handle(self, *args, **options):
        global todosgo
        print('Contando Linhas: ', end='')
        num_lines = sum([1 for line in open(options['arquivo'][0])])
        print(num_lines)

        pool = Pool(10)

        todosgo = GeneOntology.objects.values_list('nome', flat=True )

        with open(options['arquivo'][0], 'r') as file:
            reader = csv.reader(file, delimiter='\t')

            list(
                tqdm(
                    pool.imap(
                        importar,
                        reader
                    ),
                    total=num_lines)
            )
