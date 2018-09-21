from django.contrib import admin
from .models import (
    Especime,
    ClasseQuimica,
    Especie,
    Eluente,
    Aliquota,
    Familia,
    Fracao,
    Fracionamento,
    Genero,
    OrgaoDePlanta,
    Amostra,
    Sequenciamento,
    TipoDeAliquota,
    TipoDeFracionamento,
    Composto,
    PlacaTLC,
    DadosTLC,
    Algoritmo,
    GeneOntology,
    GeneInfo,
    Database,
    Sequencia
)


class EspecimeAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'data_da_coleta', 'lat', 'lng',
        'altitude', 'solo', 'vegetacao', 'altura', 'diametro', 'notas') 


class AliquotaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'tipo'
    )

class EluenteAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 
    )


class FracaoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )


class FracionamentoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )


class CompostoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'fracao'
    )


class SequenciaAdmin(admin.ModelAdmin):
    list_display = (
        'qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 
        'qend', 'sstart', 'send', 'evalue', 'bitscore', 'geneid', 'ncbitaxon', 
        'ltaxon', 'repid', 'clustername', 'station'
    )


class SequenciamentoAdmin(admin.ModelAdmin):
    list_display = (
        'data', 'algoritmo', 'database'
    )

    fields = ('data', 'algoritmo', 'database', 'texto')

    def texto(self, obj):
        return "lero"


admin.site.register(Especime, EspecimeAdmin)
admin.site.register(ClasseQuimica)
admin.site.register(Especie)
admin.site.register(Eluente, EluenteAdmin)
admin.site.register(Aliquota, AliquotaAdmin)
admin.site.register(Familia)
admin.site.register(Fracao, FracaoAdmin)
admin.site.register(Fracionamento, FracionamentoAdmin)
admin.site.register(Genero)
admin.site.register(OrgaoDePlanta)
admin.site.register(Amostra)
admin.site.register(Sequenciamento, SequenciamentoAdmin)
admin.site.register(TipoDeAliquota)
admin.site.register(Composto, CompostoAdmin)
admin.site.register(TipoDeFracionamento)
admin.site.register(PlacaTLC)
admin.site.register(DadosTLC)
admin.site.register(Algoritmo)
admin.site.register(GeneOntology)
admin.site.register(GeneInfo)
admin.site.register(Database)
admin.site.register(Sequencia, SequenciaAdmin)