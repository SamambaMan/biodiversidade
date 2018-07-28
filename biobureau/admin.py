from django.contrib import admin
from .models import (
    Amostra,
    ClasseQuimica,
    Especie,
    Eluente,
    Extrato,
    Familia,
    Fracao,
    Fracionamento,
    Genero,
    OrgaoDePlanta,
    ParteDePlanta,
    Sequenciamento,
    TipoDeExtrato,
)


class AmostraAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'data_da_coleta', 'lat', 'lng',
        'altitude', 'solo', 'vegetacao', 'altura', 'diametro', 'notas') 


class ExtratoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'tipo'
    )

class EluenteAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'polar'
    )


class FracaoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'eluente'
    )

class FracionamentoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'classe_quimica', 'positivo'
    )

admin.site.register(Amostra, AmostraAdmin)
admin.site.register(ClasseQuimica)
admin.site.register(Especie)
admin.site.register(Eluente, EluenteAdmin)
admin.site.register(Extrato, ExtratoAdmin)
admin.site.register(Familia)
admin.site.register(Fracao, FracaoAdmin)
admin.site.register(Fracionamento, FracionamentoAdmin)
admin.site.register(Genero)
admin.site.register(OrgaoDePlanta)
admin.site.register(ParteDePlanta)
admin.site.register(Sequenciamento)
admin.site.register(TipoDeExtrato)
