from django.contrib import admin

from animais.models import Animal

from datetime import date


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nm_animal', 'cd_animal_mae', 'proprietario', 'nascimento', 'anos', 'meses', 'id_sexo', 
                    'proximo_parto', 'id_mamando')  # definindo o que será exibido na listagem
    list_filter = ('id_situacao', 'id_sexo', 'id_mamando')  #definindo os filtros
    search_fields = ['nm_animal', ]

    def proprietario(self, obj):
        return obj.cd_pessoa.first_name
    proprietario.short_description = "Prop."

    def anos(self, obj):
       if (not obj.dt_nascimento):
           return None
       today = date.today()
       if (today.month >= obj.dt_nascimento.month):
           return today.year - obj.dt_nascimento.year
       else:
           return today.year - obj.dt_nascimento.year - 1

    def meses(self, obj):
       if (not obj.dt_nascimento):
           return None
       today = date.today()
       if (today.month >= obj.dt_nascimento.month):
           return today.month - obj.dt_nascimento.month
       else:
           return today.month + (12-obj.dt_nascimento.month)

    def nascimento(self, obj):
       if (obj.dt_nascimento):
           return obj.dt_nascimento.strftime("%d/%m/%y")
       else:
           return None

    def proximo_parto(sef, obj):
       if (obj.dt_pegou_cria):
          return date.fromordinal(obj.dt_pegou_cria.toordinal()+283).strftime("%d/%m/%y")
       else:
          return None
    proximo_parto.short_description = "Próx. Parto" #renomeando o label do campo, mesmo sendo obtido através de funcao 


# Register your models here.
admin.site.site_header = "Manica's Farm"  #alterando o título do software
admin.site.register(Animal, AnimalAdmin)
