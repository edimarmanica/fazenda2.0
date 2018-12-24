from django.db import models

from django.contrib.auth.models import User

CHOICES_SEXO = (
  (0, "F"),
  (1, "M"),
)

CHOICES_SITUACAO = (
  (1, "Normal"),
  (2, "Vendido"),
  (3, "Morreu"),
  (4, "Terc. Ativo"), #quando é do vô
  (5, "Terc. Inativo"),
)

CHOICES_SIM_NAO = (
  (0, "Não"),
  (1, "Sim")
)

CHOICES_COR = (
  (1, "Branca"),
  (2, "Preta"),
  (3, "Holandês"),
  (4, "Vermelha"),
  (5, "Amarela"),
  (6, "Fumaça"),
)

CHOICES_FLUXO = (
  (0, "Saída"),
  (1, "Entrada")
)

# Create your models here.
class Animal(models.Model):
    nm_animal = models.CharField(max_length=30, verbose_name="Nome")
    id_sexo = models.IntegerField(choices=CHOICES_SEXO, verbose_name="Sexo")
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento", blank=True, null=True)
    id_mamando = models.IntegerField(choices=CHOICES_SIM_NAO, verbose_name="Mamando", default=1)
    id_situacao = models.IntegerField(choices=CHOICES_SITUACAO, verbose_name="Situação", default=1)
    id_cor = models.IntegerField(choices=CHOICES_COR, verbose_name="Cor", blank=True, null=True)
    cd_animal_mae = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, verbose_name="Mãe", related_name="mae", limit_choices_to={'id_sexo':0})
    cd_animal_pai = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, verbose_name="Pai", related_name="pai", limit_choices_to={'id_sexo':1})
    cd_pessoa = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Proprietário")
    vl_venda = models.FloatField(verbose_name="Valor de Venda", blank=True, null=True)
    dt_venda = models.DateField(verbose_name="Data de Venda/Morte", blank=True, null=True)
    dt_pegou_cria = models.DateField(verbose_name="Data Pegou Cria", blank=True, null=True)
    cd_touro_pegou_cria = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, verbose_name="Touro Pegou Cria", related_name="marido", limit_choices_to={'id_sexo':1})
    ds_observacao = models.TextField(verbose_name="Observação", blank=True, null=True)
    
    def __str__(self):
       return self.get_id_situacao_display() + ": " + self.nm_animal
   
    def save(self, force_insert=False, force_update=False):
        self.nm_animal = self.nm_animal.upper()
        super(Animal, self).save(force_insert, force_update)

    class Meta:
        ordering = ["id_situacao", "-dt_nascimento", "nm_animal"] # - para ordem decrescente   -- está ordenando nos select e combobox
        verbose_name="Animal" #nome do objetos dessa tabela
        verbose_name_plural="Animais" #nome dos objetos dessa tabela no plural

class VendaCompra(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name="animal")
    data = models.DateField()
    fluxo = models.IntegerField(choices=CHOICES_FLUXO, verbose_name="Fluxo")
    peso = models.FloatField("Peso (Kg)", blank=True, null=True)
    valor_kg = models.FloatField(verbose_name="Valor/Kg", blank=True, null=True)
    valor_total = models.FloatField(verbose_name="Valor Total")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    
    def __str__(self):
        return self.animal.nm_animal + ' (' + self.data.strftime("%d/%m/%y") + ")"
    
    class Meta:
        ordering = ["-data"]