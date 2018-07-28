import uuid
from django.db import models


class Familia(models.Model):
    "Armazena Famílias de espécies de plantas"
    class Meta:
        verbose_name = "Família"

    nome = models.CharField(max_length=100)
    def __str__(self):
        if self:
            return self.nome


class Genero(models.Model):
    "Armazena o Gênero das espécies de plantas"
    class Meta:
        verbose_name = "Gênero"

    nome = models.CharField(max_length=100)
    familia = models.ForeignKey('Familia')
    
    def __str__(self):
        if self:
            return "%s %s" % (self.familia, self.nome)


class Especie(models.Model):
    """Armazena espécies de plantas
       Não armazena a planta em sí, apenas o catálogo
       de espécies de plantas disponíveis"""
    class Meta:
        verbose_name = "Espécie"
    
    nome = models.CharField(max_length=100)
    common = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Nome popular desta espécie de planta, ex.: pitangueira")
    genero = models.ForeignKey('Genero')

    def __str__(self):
        if self:
            return "%s %s" % (self.genero, self.nome)


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

    def __str__(self):
        if self:
            return self.orgao


class Amostra(models.Model):
    """Dados cadastrais da coleta de uma amostra de planta.
       Aqui estarão armazenados os dados da coleta da 
       planta (sua esécie, tamanho, local, etc.)"""
    identificador = models.UUIDField(
        editable=False,
        default=uuid.uuid4
        )
    especie = models.ForeignKey('Especie')
    data_da_coleta = models.DateTimeField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)
    solo = models.CharField(max_length=200, blank=True, null=True)
    vegetacao = models.CharField(
        max_length=200,
        verbose_name="Vegetação",
        blank=True,
        null=True
    )
    altura = models.FloatField(blank=True, null=True)
    diametro = models.FloatField(verbose_name="Diâmetro", blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        if self:
            return "%s - %s" % (
                str(self.identificador)[:6],
                self.especie
            )



class ParteDePlanta(models.Model):
    "Dados da parte da planta coletada no campo"
    orgao = models.ForeignKey('OrgaoDePlanta')
    amostra = models.ForeignKey('Amostra')
    cor = models.CharField(max_length=50, blank=True, null=True)
    cheiro = models.CharField(max_length=50, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        if self:
            return "%s - %s" % (
                self.amostra,
                self.orgao
            )
        return ""


class Eluente(models.Model):
    nome = models.CharField(max_length=100)
    polar = models.BooleanField()
    def __str__(self):
        if self:
            return self.nome



class ClasseQuimica(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        if self:
            return self.nome


class TipoDeExtrato(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        if self:
            return self.nome


class Extrato(models.Model):
    data = models.DateField()
    tipo = models.ForeignKey('TipoDeExtrato')
    parte_de_planta = models.ForeignKey('ParteDePlanta')

    def __str__(self):
        if self:
            return str(self.parte_de_planta)


class Sequenciamento(models.Model):
    data = models.DateField(verbose_name="Data do Sequenciamento Genético")
    extrato = models.ForeignKey('Extrato')
    arquivo_fasta = models.CharField(max_length=1000)

    def __str__(self):
        if self:
            return str(self.extrato)


class Fracao(models.Model):
    class Meta:
        verbose_name = "Fração"
        verbose_name_plural = "Frações"

    extrato = models.ForeignKey('Extrato')
    eluente = models.ForeignKey('Eluente')

    def __str__(self):
        if self:
            return "%s-F%s" % (
                self.extrato,
                self.id
            )


class Fracionamento(models.Model):
    fracao = models.ForeignKey('Fracao')
    classe_quimica = models.ForeignKey('ClasseQuimica')
    positivo = models.BooleanField()

    def __str__(self):
        if self:
            return "%sFR%s" % (
                self.fracao,
                self.id
            )
