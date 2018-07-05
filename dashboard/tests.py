from django.test import TestCase
from .views import serializa
from collections import OrderedDict
import pandas as pd


parametro = [
            OrderedDict({
                "familia": "carinha",
                "genero": "generinho",
                "especie": "especinha",
                "count": 127
            })
        ]


class TesteSerializa(TestCase):
    def test_serializa_listagem(self):
        retorno = serializa(parametro)
        assert [['carinha', 'generinho', 'especinha', 127]] == retorno

    def test_importa_pandas(self):
        frame = pd.DataFrame(parametro)
        import ipdb; ipdb.set_trace()

