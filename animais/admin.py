from django.contrib import admin

from animais.models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nm_animal', 'dt_nascimento')  # definindo o que será exibido na listagem
    list_filter = ('id_sexo', )

# Register your models here.
admin.site.register(Animal, AnimalAdmin)
