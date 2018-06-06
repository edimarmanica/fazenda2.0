from django.contrib import admin

from caixa.models import Tipo, Caixa
from functions.utils import DateUtils

class CaixaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'pessoa_fmt', 'tipo', 'fluxo', 'vencimento_fmt', 'pagamento_fmt', 'valor')  # definindo o que será exibido na listagem
    list_filter = ('vencimento', 'pagamento')  #definindo os filtros
    search_fields = ['descricao', ]
    actions = ['proximo_mes', ]

    def fluxo(self, obj):
        return obj.tipo.fluxo
    
    def pessoa_fmt(self, obj):
        return obj.pessoa.first_name;
    pessoa_fmt.short_description = "Pessoa"
    
    def vencimento_fmt(self, obj):
        return DateUtils.format(obj.vencimento)
    vencimento_fmt.short_description = "Vencimento"
    
    def pagamento_fmt(self, obj):
        return DateUtils.format(obj.pagamento)
    pagamento_fmt.short_description = "Pagamento"
    
    def proximo_mes(modeladmin, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.vencimento = DateUtils.future_months(obj.vencimento, 1)
            obj.pagamento = None
            obj.save()
    proximo_mes.short_description = "Gerar próximo vencimento"

admin.site.register(Tipo)
admin.site.register(Caixa, CaixaAdmin)

