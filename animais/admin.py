from django.contrib import admin

from animais.models import Animal

from datetime import date


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nm_animal', 'cd_animal_mae', 'cd_pessoa', 'nascimento', 'anos', 'meses', 'id_sexo', 'id_situacao', 
                    'proximo_parto', 'id_mamando', 'id_cor')  # definindo o que será exibido na listagem
    list_filter = ('id_situacao', 'id_sexo', 'id_mamando')  #definindo os filtros

    def anos(self, obj):
       today = date.today()
       if (today.month >= obj.dt_nascimento.month):
           return today.year - obj.dt_nascimento.year
       else:
           return today.year - obj.dt_nascimento.year - 1

    def meses(self, obj):
       today = date.today()
       if (today.month >= obj.dt_nascimento.month):
           return today.month - obj.dt_nascimento.month
       else:
           return today.month + (12-obj.dt_nascimento.month)

    def nascimento(self, obj):
       return obj.dt_nascimento.strftime("%d/%m/%y")

    def proximo_parto(sef, obj):
       if (obj.dt_pegou_cria):
          return date.fromordinal(obj.dt_pegou_cria.toordinal()+283).strftime("%d/%m/%y")
       else:
          return None


# Register your models here.
admin.site.register(Animal, AnimalAdmin)
