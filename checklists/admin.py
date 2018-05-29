from django.contrib import admin

from checklists.models import Item,Tipo,ItemTipo

class ItemTipoTabularInline(admin.TabularInline):
    model = ItemTipo

class TipoAdmin(admin.ModelAdmin):
    inlines = [ItemTipoTabularInline]
    class Meta:
        model = Tipo

# Register your models here.
admin.site.register(Item)
admin.site.register(Tipo, TipoAdmin)

