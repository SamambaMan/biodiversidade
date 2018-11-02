import json
from django.core.management import BaseCommand
from memoized import memoized
from biobureau.models import (
    Familia,
    FonteFamilia
)


@memoized
def obter_familia(familia):
    n_familia = Familia.objects.filter(nome=familia).first()

    if not n_familia:
        n_familia = Familia()
        n_familia.nome = familia
        n_familia.save()

    return n_familia


@memoized
def obter_fonte(fonte):
    n_fonte = FonteFamilia.objects.filter(name=fonte).first()

    if not n_fonte:
        n_fonte = FonteFamilia()
        n_fonte.name = fonte
        n_fonte.save()

    return n_fonte


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arquivo', nargs=1, type=str)
        parser.add_argument('fonte', nargs=1, type=str)

    def handle(self, *args, **options):
        arquivo = options['arquivo'][0]
        fonte = options['fonte'][0]

        fonte = obter_fonte(fonte)

        with open(arquivo, 'r') as arquivo:
            familias = json.load(arquivo)

        for familia in familias:
            print(familia)
            n_familia = obter_familia(familia)
            n_familia.fonte.add(fonte)
