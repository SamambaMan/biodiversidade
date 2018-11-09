import csv
from tqdm import tqdm
from django.core.management import BaseCommand
from memoized import memoized
from biobureau.models import GeneOntology


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arquivo', nargs=1, type=str)
    
    def handle(self, *args, **options):
        print('Contando Linhas: ', end='')
        num_lines = sum([1 for line in open(options['arquivo'][0])])
        print(num_lines)
        with open(options['arquivo'][0], 'r') as file:
            reader = csv.reader(file, delimiter='\t')

            for linha in tqdm(reader, total=num_lines):
                go = GeneOntology.objects.filter(nome=linha[0]).first()
                if go:
                    go.descricao = linha[1]
                    go.save()
            