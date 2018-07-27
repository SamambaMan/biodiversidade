from django.db import models


class Familia(models.Model):
    "Armazena Famílias de espécies de plantas"
    class Meta:
        verbose_name = "Família"

    nome = models.CharField(max_length=100)


class Genero(models.Model):
    "Armazena o Gênero das espécies de plantas"
    class Meta:
        verbose_name = "Gênero"

    nome = models.CharField(max_length=100)
    familia = models.ForeignKey('Familia')


class Especie(models.Model):
    """Armazena espécies de plantas
       Não armazena a planta em sí, apenas o catálogo
       de espécies de plantas disponíveis"""
    class Meta:
        verbose_name = "Espécie"
    
    nome = models.CharField(max_length=100)
    common = models.CharField(
        max_length=200,
        help_text="Nome popular desta espécie de planta, ex.: pitangueira")
    genero = models.ForeignKey('Genero')


class OrgaoDePlanta(models.Model):
    """Catálogo de órgãos de plantas (raíz, caule, etc)
       O órgão da planta é compartilhado entre diversas
       espécies, portanto, aqui armazenaremos o catálogo
       destas partes para serem utilizados nas amostras
       de plantas e suas partes posteriormente"""
    class Meta:
        verbose_name = "Órgão de Planta"

    orgao = models.CharField(
        max_length=100,
        verbose_name="Órgão")


class Amostra(models.Model):
    """Dados cadastrais da coleta de uma amostra de planta.
       Aqui estarão armazenados os dados da coleta da 
       planta (sua esécie, tamanho, local, etc.)"""
    identificador = models.CharField(
        max_length=50,
        help_text="Identificador único de uma amostra. Deverá "
                  "seguir uma taxonomia definida posteriormente")
    especie = models.ForeignKey('Especie')
    data_da_coleta = models.DateTimeField()
    lat = models.FloatField()
    lng = models.FloatField()
    altitude = models.IntegerField()
    solo = models.CharField(max_length=200)
    vegetacao = models.CharField(
        max_length=200,
        verbose_name="Vegetação"
    )
    altura = models.FloatField()
    diametro = models.FloatField(verbose_name="Diâmetro")
    notas = models.TextField()


class ParteDePlanta(models.Model):
    "Dados da parte da planta coletada no campo"
    orgao = models.ForeignKey('OrgaoDePlanta')
    amostra = models.ForeignKey('Amostra')
    cor = models.CharField(max_length=50)
    cheiro = models.CharField(max_length=50)
    peso = models.FloatField()
    notas = models.TextField()


class Sequenciamento(models.Model):
    data = models.DateField(verbose_name="Data do Sequenciamento Genético")
    amostra = models.ForeignKey('Amostra')
    arquivo_fasta = models.CharField(max_length=1000)


class Eluente(models.Model):
    nome = models.CharField(max_length=100)
    polar = models.BooleanField()


class Extrato(models.Model):
    data = models.DateField()
    parte_de_planta = models.ForeignKey('ParteDePlanta')


class Ensaio(models.Model):
    extrato = models.ForeignKey('Extrato')
    classe_quimica = models.ForeignKey('ClasseQuimica')
    eluente = models.ForeignKey('Eluente')


class ClasseQuimica(models.Model):
    nome = models.CharField(max_length=50)



