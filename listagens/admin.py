# coding=utf8
from django.contrib import admin
from listagens.models import Biodiversidade, Estacoes
from django.core.exceptions import ValidationError

# Register your models here.

class EstacoesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'classificacao', 'hshannon', 'latitude', 'longitude',
    )

    search_fields = ('id', )

class BiodiversidadeAdmin(admin.ModelAdmin):
    search_fields = ('species',)
    list_display = ('id', 'species', 'algorithm', 'database', 'qseqid',
                    'sseqid', 'pident', 'length', 'mismatch', 'gapopen',
                    'qstart', 'qend', 'sstart', 'send', 'evalue',
                    'bitscore', 'gi', 'geneid', 'ncbitaxon', 'ltaxon',
                    'repid', 'clustername', 'obs', 'station', 'lat',
                    'long', 'original_seq_code', 'source', 'lat2',
                    'long2', 'frequency', 'string1', 'string2', 'string3',
                    'string4')

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(
            BiodiversidadeAdmin,
            self).get_search_results(
                request,
                queryset,
                search_term)

        queryset = Biodiversidade.objects.filter()

        termos = search_term.split(";")

        ultimotermo = ""

        try:
            for termo in termos:

                busca = termo.split(":")
                ultimotermo = busca[0]

                if busca[0] == "species":
                    queryset = queryset.filter(species__contains=busca[1])
                elif busca[0] == "algorithm":
                    queryset = queryset.filter(algorithm__contains=busca[1])
                elif busca[0] == "database":
                    queryset = queryset.filter(database__contains=busca[1])
                elif busca[0] == "qseqid":
                    queryset = queryset.filter(qseqid__contains=busca[1])
                elif busca[0] == "sseqid":
                    queryset = queryset.filter(sseqid__contains=busca[1])
                elif busca[0] == "pident":
                    queryset = queryset.filter(pident__contains=busca[1])
                elif busca[0] == "length":
                    queryset = queryset.filter(length__contains=busca[1])
                elif busca[0] == "mismatch":
                    queryset = queryset.filter(mismatch__contains=busca[1])
                elif busca[0] == "gapopen":
                    queryset = queryset.filter(gapopen__contains=busca[1])
                elif busca[0] == "qstart":
                    queryset = queryset.filter(qstart__contains=busca[1])
                elif busca[0] == "qend":
                    queryset = queryset.filter(qend__contains=busca[1])
                elif busca[0] == "sstart":
                    queryset = queryset.filter(sstart__contains=busca[1])
                elif busca[0] == "send":
                    queryset = queryset.filter(send__contains=busca[1])
                elif busca[0] == "evalue":
                    queryset = queryset.filter(evalue__contains=busca[1])
                elif busca[0] == "bitscore":
                    queryset = queryset.filter(bitscore__contains=busca[1])
                elif busca[0] == "gi":
                    queryset = queryset.filter(gi__contains=busca[1])
                elif busca[0] == "geneid":
                    queryset = queryset.filter(geneid__contains=busca[1])
                elif busca[0] == "ncbitaxon":
                    queryset = queryset.filter(ncbitaxon__contains=busca[1])
                elif busca[0] == "ltaxon":
                    queryset = queryset.filter(ltaxon__contains=busca[1])
                elif busca[0] == "repid":
                    queryset = queryset.filter(repid__contains=busca[1])
                elif busca[0] == "clustername":
                    queryset = queryset.filter(clustername__contains=busca[1])
                elif busca[0] == "obs":
                    queryset = queryset.filter(obs__contains=busca[1])
                else:
                    queryset = Biodiversidade.objects.filter()
        except:
            queryset = Biodiversidade.objects.filter(species=None)

        return queryset, use_distinct

admin.site.site_title = u'Biodiversidade'
admin.site.site_header = u'Biodiversidade'
admin.site.index_title = u'Biodiversidade'

admin.site.register(Biodiversidade, BiodiversidadeAdmin)
admin.site.register(Estacoes, EstacoesAdmin)