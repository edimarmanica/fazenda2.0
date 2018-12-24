# Classes do django
from django.contrib import admin
from datetime import date
from functions.utils import DateUtils #função que eu criei
from rangefilter.filter import DateRangeFilter #Fonte: https://github.com/silentsokolov/django-admin-rangefilter

#classes minhas
from animais.models import Animal, VendaCompra

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nm_animal', 'cd_animal_mae', 'proprietario', 'nascimento', 'anos', 'meses', 'id_sexo', 
                    'proximo_parto', 'id_mamando')  # definindo o que será exibido na listagem
    list_filter = ('id_situacao', 'id_sexo', 'id_mamando')  #definindo os filtros
    search_fields = ['nm_animal', ]

    def proprietario(self, obj):
        if (obj.cd_pessoa):
            return obj.cd_pessoa.first_name
        else:
            return None
    proprietario.short_description = "Prop."

    def anos(self, obj):
       return DateUtils.age_years(obj.dt_nascimento)

    def meses(self, obj):
       return DateUtils.age_months(obj.dt_nascimento)

    def nascimento(self, obj):
        return DateUtils.format(obj.dt_nascimento)

    def proximo_parto(sef, obj):
        parto = DateUtils.future_days(obj.dt_pegou_cria, 283)
        if parto and parto > date.today():
            return DateUtils.format(parto)
        else:
            return None;
    proximo_parto.short_description = "Próx. Parto" #renomeando o label do campo, mesmo sendo obtido através de funcao 

class VendaCompraAdmin(admin.ModelAdmin):
    list_display = ('animal', 'data_fmt', 'fluxo', 'peso', 'valorKg', 'valorTotal')  # definindo o que será exibido na listagem
    list_filter = (('data', DateRangeFilter), )  #definindo os filtros

    def data_fmt(self, obj):
        return DateUtils.format(obj.data)
    data_fmt.short_description = "Data"
    

# Register your models here.
admin.site.register(Animal, AnimalAdmin)
admin.site.register(VendaCompra, VendaCompraAdmin)
