from django.contrib import admin

from animais.models import Animal

from datetime import date
from functions.formatters import DateFormatter #função que eu criei


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
       return DateFormatter.anos(obj.dt_nascimento)

    def meses(self, obj):
       return DateFormatter.meses(obj.dt_nascimento)

    def nascimento(self, obj):
        return DateFormatter.format(obj.dt_nascimento)

    def proximo_parto(sef, obj):
       if (obj.dt_pegou_cria):
          return date.fromordinal(obj.dt_pegou_cria.toordinal()+283).strftime("%d/%m/%y")
       else:
          return None
    proximo_parto.short_description = "Próx. Parto" #renomeando o label do campo, mesmo sendo obtido através de funcao 


# Register your models here.
admin.site.site_header = "Manica's Farm"  #alterando o título do software
admin.site.register(Animal, AnimalAdmin)
