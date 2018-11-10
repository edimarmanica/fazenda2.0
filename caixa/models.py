from django.db import models

from django.contrib.auth.models import User

CHOICES_FLUXO = (
  (1, "Entrada"),
  (2, "Saída"),
)


class Tipo(models.Model):
    nome = models.CharField(max_length=30)
    fluxo = models.IntegerField(choices=CHOICES_FLUXO)
    tipo_pai = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name="pai",
                                 limit_choices_to={'tipo_pai':None})
    codigo_bb = models.IntegerField(blank=True, null=True, verbose_name="Código BB")

    def __str__(self):
        return self.nome

class Caixa(models.Model):
    descricao = models.CharField(max_length=30, verbose_name="Descrição")
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="tipo",
                                 limit_choices_to={'tipo_pai':None})
    pessoa = models.ForeignKey(User, on_delete=models.PROTECT)
    valor = models.FloatField()
    vencimento = models.DateField()
    pagamento = models.DateField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    
    def __str__(self):
        return self.descricao + ' (' + self.vencimento.strftime("%d/%m/%y") + ")"
    


    
