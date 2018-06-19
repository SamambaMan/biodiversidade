from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Biodiversidade(models.Model):
    species = models.CharField(max_length=200, null=True, blank=True, verbose_name="Species", help_text="species")
    algorithm = models.CharField(max_length=200, null=True, blank=True, verbose_name="Algorithm", help_text="algorithm")
    database = models.CharField(max_length=200, null=True, blank=True, verbose_name="Database", help_text="database")
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
    gi = models.CharField(max_length=5000, null=True, blank=True, verbose_name="GI", help_text="gi")
    geneid = models.CharField(max_length=200, null=True, blank=True, verbose_name="GeneID", help_text="geneid")
    ncbitaxon = models.CharField(max_length=200, null=True, blank=True, verbose_name="NCBI-taxon", help_text="ncbitaxon")
    ltaxon = models.CharField(max_length=200, null=True, blank=True, verbose_name="Lowest taxon of the cluster", help_text="ltaxon")
    repid = models.CharField(max_length=200, null=True, blank=True, verbose_name="RepID", help_text="repid")
    clustername = models.CharField(max_length=500, null=True, blank=True, verbose_name="Cluster Name", help_text="clustername")
    obs = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Obs", help_text="obs")
    station = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    original_seq_code = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    lat2 = models.FloatField(blank=True, null=True)
    long2 = models.FloatField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    string1 = models.CharField(max_length=255, blank=True, null=True)
    string2 = models.CharField(max_length=255, blank=True, null=True)
    string3 = models.CharField(max_length=255, blank=True, null=True)
    string4 = models.CharField(max_length=255, blank=True, null=True)

class Estacoes(models.Model):
    id = models.CharField(verbose_name="id", max_length=255, primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    profundidade = models.TextField(blank=True, null=True)
    hshannon = models.FloatField(blank=True, null=True)
    parametro_2 = models.FloatField(blank=True, null=True)
    parametro_3 = models.FloatField(blank=True, null=True)
    parametro_4 = models.FloatField(blank=True, null=True)
    parametro_5 = models.FloatField(blank=True, null=True)
    parametro_6 = models.FloatField(blank=True, null=True)
    parametro_7 = models.FloatField(blank=True, null=True)
    parametro_8 = models.FloatField(blank=True, null=True)
    parametro_9 = models.FloatField(blank=True, null=True)
    parametro_10 = models.FloatField(blank=True, null=True)
    parametro_11 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    classificacao = models.TextField(blank=True, null=True)
    fonte = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacoes'


class Especies(models.Model):
    row_names = models.TextField(db_column='row.names', blank=True, null=True)
    cod = models.FloatField(db_column='COD', blank=True, null=True)
    item_taxonomico = models.NullBooleanField(db_column='Item Taxonomico')
    código_item_taxonomico = models.NullBooleanField(db_column='Código Item Taxonomico')
    item_taxonomico_superior = models.NullBooleanField(db_column='Item Taxonomico Superior')
    codigo_item_taxononico_superior = models.NullBooleanField(db_column='Codigo Item Taxononico Superior')
    nome_atribuido = models.TextField(db_column='Nome Atribuido', blank=True, null=True)
    filo = models.TextField(db_column='Filo', blank=True, null=True)
    classe = models.TextField(db_column='Classe', blank=True, null=True)
    ordem = models.TextField(db_column='Ordem', blank=True, null=True)
    familia = models.TextField(db_column='Familia', blank=True, null=True)
    genero = models.NullBooleanField(db_column='Genero')
    especie = models.TextField(db_column='Especie', blank=True, null=True)
    fonte = models.TextField(db_column='Fonte', blank=True, null=True)
    amostras = models.TextField(db_column='Amostras', blank=True, null=True)
    taxonid = models.TextField(db_column='TaxonID', blank=True, null=True)
    rank = models.TextField(db_column='Rank', blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especies'


