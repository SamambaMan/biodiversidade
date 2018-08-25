import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


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


class Especime(models.Model):
    """Dados cadastrais da coleta de uma amostra de planta.
       Aqui estarão armazenados os dados da coleta da 
       planta (sua esécie, tamanho, local, etc.)"""
    class Meta:
        verbose_name = 'Espécime'

    identificador = models.UUIDField(
        editable=False,
        default=uuid.uuid4
        )
    especie = models.ForeignKey('Especie', verbose_name='Espécie')
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
    ponto_de_referencia = models.CharField(max_length=200, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    nome_comum = models.CharField(blank=True, null=True, max_length=200)
    autor = models.CharField(max_length=200, blank=True, null=True)
    light = models.IntegerField(blank=True, null=True)
    abund = models.IntegerField(blank=True, null=True)
    photonum = ArrayField(
        models.IntegerField(blank=True, null=True),
        blank=True, null=True
    )
    numero_individuos = models.IntegerField(blank=True, null=True)
    etnologico = models.CharField(max_length=200, blank=True, null=True)
    identid = models.IntegerField(blank=True, null=True)
    nome_erva = models.CharField(max_length=200, blank=True, null=True)
    data_erva = models.DateField(blank=True, null=True)

    def __str__(self):
        if self:
            return "%s - %s" % (
                str(self.identificador)[:6],
                self.especie
            )


class Amostra(models.Model):
    "Dados da parte da planta coletada no campo"
    orgao = models.ForeignKey('OrgaoDePlanta')
    amostra = models.ForeignKey('Especime')
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


class TipoDeAliquota(models.Model):
    class Meta:
        verbose_name = 'Tipo de Alíquota'
        verbose_name_plural = 'Tipos de Alíquota'

    nome = models.CharField(max_length=50)
    def __str__(self):
        if self:
            return self.nome


class Aliquota(models.Model):
    class Meta:
        verbose_name = 'Alíquota'
        verbose_name_plural = 'Alíquotas'
    data = models.DateField()
    tipo = models.ForeignKey('TipoDeAliquota')
    amostra = models.ForeignKey('Amostra')

    def __str__(self):
        if self:
            return str(self.amostra)


class Sequenciamento(models.Model):
    data = models.DateField(verbose_name="Data do Sequenciamento Genético")
    aliquota = models.ForeignKey('Aliquota')
    arquivo_fasta = models.CharField(max_length=1000)

    def __str__(self):
        if self:
            return str(self.aliquota)


class TipoDeFracionamento(models.Model):
    class Meta:
        verbose_name = 'Tipo de Fracionamento'
        verbose_name_plural = 'Tipos de Fracionamento'
    nome = models.CharField(max_length=50)
    def __str__(self):
        if self:
            return self.nome


class Fracionamento(models.Model):
    aliquota = models.OneToOneField('Aliquota')
    tipo_de_fracionamento = models.ForeignKey('TipoDeFracionamento')
    

    def __str__(self):
        if self:
            return "%s-F%s" % (
                self.aliquota,
                self.id
            )


class Fracao(models.Model):
    class Meta:
        verbose_name = "Fração"
        verbose_name_plural = "Frações"

    eluente = models.ForeignKey('Eluente')
    fracionamento = models.ForeignKey('Fracionamento')

    def __str__(self):
        if self:
            return "%sFR%s" % (
                self.fracionamento,
                self.id
            )


class Composto(models.Model):
    fracao = models.ForeignKey('Fracao')
    classe_quimica = models.ForeignKey('ClasseQuimica')
    positivo = models.BooleanField()
    notas = models.TextField(blank=True, null=True)
    percentual_de_pureza = models.FloatField(blank=True, null=True)
    notas_sobre_pureza = models.TextField(blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    solvente = models.CharField(max_length=50, blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    formula = models.CharField(max_length=50, blank=True, null=True)
    nome_comum = models.CharField(max_length=50, blank=True, null=True)
    nome_IUPAC = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self:
            return self.nome_comum
