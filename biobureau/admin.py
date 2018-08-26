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
    DadosTLC
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
admin.site.register(Sequenciamento)
admin.site.register(TipoDeAliquota)
admin.site.register(Composto, CompostoAdmin)
admin.site.register(TipoDeFracionamento)
admin.site.register(PlacaTLC)
admin.site.register(DadosTLC)