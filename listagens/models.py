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

