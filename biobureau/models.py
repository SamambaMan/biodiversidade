import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


class FonteFamilia(models.Model):
    class Meta:
        verbose_name = 'Fonte de Família'
        verbose_name_plural = 'Fontes de Família'

    name = models.CharField(max_length=100)
    def __str__(self):
        if self:
            return self.name


class Familia(models.Model):
    "Armazena Famílias de espécies de plantas"
    class Meta:
        verbose_name = "Família"

    nome = models.CharField(max_length=100)
    fonte = models.ManyToManyField('FonteFamilia')
    brasileira = models.BooleanField(default=False)
    taxid = models.IntegerField(blank=True, null=True)
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
            return self.nome


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
            return self.nome


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
    etnologico = models.TextField(blank=True, null=True)
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
    classe = models.CharField(max_length=100, default="Polar")
    composicao = models.CharField(max_length=100, null=True, blank=True)
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
            return str(self.data)


class Algoritmo(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        if self:
            return self.nome


class GeneOntology(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        if self:
            return self.nome

class GeneInfo(models.Model):
    identificacao = models.IntegerField()
    def __str__(self):
        if self:
            return str(self.identificacao)

class Database(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        if self:
            return self.nome

class Sequenciamento(models.Model):
    data = models.DateField(verbose_name="Data do Sequenciamento Genético")
    aliquota = models.ForeignKey('Aliquota')
    arquivo_fasta = models.CharField(max_length=1000, null=True, blank=True)
    algoritmo = models.ForeignKey('Algoritmo', blank=True, null=True)
    database = models.ForeignKey('Database', blank=True, null=True)

    def texto(self):
        return str(self.data)

    def __str__(self):
        if self:
            return str(self.data)


class ArquivoFasta(models.Model):
    sequenciamento = models.ForeignKey('sequenciamento')
    arquivo_fasta = models.CharField(max_length=1000, null=True, blank=True)


class Sequencia(models.Model):
    sequenciamento = models.ForeignKey('Sequenciamento')
    qseqid = models.CharField(max_length=200, null=True, blank=True, help_text="qseqid")
    sseqid = models.CharField(max_length=200, null=True, blank=True, help_text="sseqid")
    pident = models.CharField(max_length=200, null=True, blank=True, help_text="pident")
    length = models.CharField(max_length=200, null=True, blank=True, help_text="length")
    mismatch = models.CharField(max_length=200, null=True, blank=True, help_text="mismatch")
    gapopen = models.CharField(max_length=200, null=True, blank=True, help_text="gapopen")
    qstart = models.CharField(max_length=200, null=True, blank=True, help_text="qstart")
    qend = models.CharField(max_length=200, null=True, blank=True, help_text="qend")
    sstart = models.CharField(max_length=200, null=True, blank=True, help_text="sstart")
    send = models.CharField(max_length=200, null=True, blank=True, help_text="send")
    evalue = models.CharField(max_length=200, null=True, blank=True, help_text="evalue")
    bitscore = models.CharField(max_length=200, null=True, blank=True, help_text="bitscore")
    geneinfo = models.ManyToManyField('GeneInfo')
    geneid = models.CharField(max_length=200, null=True, blank=True, verbose_name="GeneID", help_text="geneid")
    ncbitaxon = models.CharField(max_length=200, null=True, blank=True, verbose_name="NCBI-taxon", help_text="ncbitaxon")
    ltaxon = models.CharField(max_length=200, null=True, blank=True, verbose_name="Lowest taxon of the cluster", help_text="ltaxon")
    repid = models.CharField(max_length=200, null=True, blank=True, verbose_name="RepID", help_text="repid")
    clustername = models.CharField(max_length=500, null=True, blank=True, verbose_name="Cluster Name", help_text="clustername")
    geneontology = models.ManyToManyField('GeneOntology')
    station = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self:
            return self.qseqid


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
    protocolo = models.IntegerField(blank=True, null=True)


class Fracao(models.Model):
    class Meta:
        verbose_name = "Fração"
        verbose_name_plural = "Frações"

    rt_inicial = models.FloatField(null=True, blank=True)
    rt_final = models.FloatField(null=True, blank=True)
    numero_fracao = models.IntegerField(null=True, blank=True)
    notas = models.TextField(blank=True, null=True)
    fracionamento = models.ForeignKey('Fracionamento')



class DadosTLC(models.Model):
    class Meta:
        verbose_name = "Dados TLC"
        verbose_name_plural = "Dados TLC"

    fracao = models.ForeignKey('Fracao', null=True, blank=True)
    fracionamento = models.ForeignKey('Fracionamento', null=True, blank=True)
    placa = models.ForeignKey('PlacaTLC')
    quantidade = models.FloatField(null=True, blank=True)
    linha = models.IntegerField(null=True, blank=True)
    coluna = models.IntegerField(null=True, blank=True)
    classe_quimica = models.ForeignKey('ClasseQuimica', blank=True, null=True)
    resultado = models.NullBooleanField(default=False)
    tipo_composto_tlc = models.IntegerField(null=True, blank=True)


class PlacaTLC(models.Model):
    """Agregador de Dados TLC"""
    numero_de_faixas = models.IntegerField(blank=True, null=True)
    data_da_analise = models.DateField(blank=True, null=True)
    imagem = models.ImageField(blank=True, null=True)
    eluente = models.ForeignKey('Eluente', null=True, blank=True)
    notas = models.TextField(blank=True, null=True)
    idextracta = models.IntegerField(blank=True, null=True)


class Composto(models.Model):
    fracao = models.ForeignKey('Fracao')
    data_isolamento = models.DateField(null=True, blank=True)
    depid = models.IntegerField(blank=True, null=True)
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
    smiles = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self:
            return self.nome_comum
