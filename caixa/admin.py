# Classes do django
import csv, io, datetime, locale
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect 

from django.contrib.auth.models import User

# Classes minhas
from caixa.models import Tipo, Caixa
from caixa.forms import CsvImportForm
from functions.utils import DateUtils

class CaixaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'pessoa_fmt', 'tipo', 'fluxo', 'vencimento_fmt', 'pagamento_fmt', 'valor')  # definindo o que será exibido na listagem
    list_filter = ('vencimento', 'pagamento')  #definindo os filtros
    search_fields = ['descricao', ]
    actions = ['proximo_mes', ]
    
    change_list_template = "caixa_changelist.html"

    def fluxo(self, obj):
        return obj.tipo.get_fluxo_display() # get_NOMEATRIBUTO_display() é uma função para pegar o valor dos choices
    
    def pessoa_fmt(self, obj):
        return obj.pessoa.get_full_name();
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
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls
    
    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]   
            decoded_file = csv_file.read().decode('iso-8859-1')
            reader = csv.reader(io.StringIO(decoded_file))
            next(reader, None) # pulando o cabeçalho
            nr_importacoes = 0;
            for line in reader:
                try:
                    tipo = Tipo.objects.get(codigo_bb=int(line[4]))
                    created = Caixa.objects.get_or_create(
                        descricao = "IMPORTAÇÃO BB: " +tipo.nome,
                        tipo = tipo,
                        pessoa = User.objects.get(pk=1),
                        valor = abs(float(line[5])),
                        vencimento = datetime.datetime.strptime(line[0], '%m/%d/%Y'),
                        pagamento = datetime.datetime.strptime(line[0], '%m/%d/%Y')
                    )
                    nr_importacoes += 1
                except Tipo.DoesNotExist:
                    tipo = None
            self.message_user(request, "Importações realizadas: {}".format(nr_importacoes))
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )

class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fluxo', 'tipo_pai', 'codigo_bb')  # definindo o que será exibido na listagem
    list_filter = ('tipo_pai', )  #definindo os filtros
    search_fields = ['nome', ]
    

admin.site.register(Tipo, TipoAdmin)
admin.site.register(Caixa, CaixaAdmin)

