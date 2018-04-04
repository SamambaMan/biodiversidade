from django.contrib import admin
from .models import VCompound

# Register your models here.


class VCompoundAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        #Disable delete
        actions = super(VCompoundAdmin, self).get_actions(request)
        del actions['delete_selected']
        return 

    list_display = ('sampleid',
    'origin_sampleid',
    'opeid',
    'isolationdate',
    'depid',
    'notes',
    'active',
    'remove',
    'purity_pct',
    'purity_notes',
    'quantity',
    'volume',
    'solvent',
    'mw',
    'formula',
    'name_common',
    'name_iupac',
    'smiles',
    'init',
    'initdate',
    'edit',
    'editdate',
    'operator',
    'depositor')

admin.site.register(VCompound, VCompoundAdmin)