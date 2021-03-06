# Generated by Django 2.0.5 on 2018-05-29 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0005_auto_20180528_0119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'ordering': ['-dt_nascimento'], 'verbose_name': 'Animal', 'verbose_name_plural': 'Animais'},
        ),
        migrations.AlterField(
            model_name='animal',
            name='cd_pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Proprietário'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='cd_touro_pegou_cria',
            field=models.ForeignKey(blank=True, limit_choices_to={'id_sexo': 1}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='marido', to='animais.Animal', verbose_name='Touro Pegou Cria'),
        ),
    ]
