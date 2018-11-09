from django.contrib import admin
from django import forms
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
    Sequencia,
    FonteFamilia,
    ArquivoFasta
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


class SequenciaForm(forms.ModelForm):
    class Meta:
        model = Sequencia
        fields = '__all__'
    
    gene_ontology = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea()
    )
    gene_identification = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea()
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)

        kwargs.update(initial={
            'gene_ontology': '; '.join(
                x.nome for x in list(instance.geneontology.all())
            ),
            'gene_identification': '; '.join(
                str(x.identificacao) for x in list(instance.geneinfo.all()
            ))
        })

        super().__init__(*args, **kwargs)

class SequenciaAdmin(admin.ModelAdmin):
    form = SequenciaForm
    list_display = (
        'qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 
        'qend', 'sstart', 'send', 'evalue', 'bitscore', 'geneid', 'ncbitaxon', 
        'ltaxon', 'repid', 'clustername', 'station'
    )

    fields = (
        'qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 
        'qend', 'sstart', 'send', 'evalue', 'bitscore', 'geneid', 'ncbitaxon', 
        'ltaxon', 'repid', 'clustername', 'station', 'gene_ontology', 'gene_identification'
    )


class ArquivoFastaInline(admin.TabularInline):
    model = ArquivoFasta


class SequenciamentoAdmin(admin.ModelAdmin):
    list_display = (
        'data', 'algoritmo', 'database'
    )
    inlines = [
        ArquivoFastaInline
    ]


class FamiliaAdmin(admin.ModelAdmin):
    search_fields = ['nome']


admin.site.register(Especime, EspecimeAdmin)
admin.site.register(ClasseQuimica)
admin.site.register(Especie)
admin.site.register(Eluente, EluenteAdmin)
admin.site.register(Aliquota, AliquotaAdmin)
admin.site.register(Familia, FamiliaAdmin)
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
admin.site.register(FonteFamilia)