from django.db import models

# Create your models here.
class Item(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=30)
    itens = models.ManyToManyField(Item, through='ItemTipo')

    def __str__(self):
        return self.nome

class ItemTipo(models.Model):  #NXN com atributos
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()

    class Meta:
        unique_together = (('tipo', 'item'),)

