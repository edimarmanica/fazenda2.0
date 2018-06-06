# Generated by Django 2.0.5 on 2018-05-29 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('fluxo', models.IntegerField(choices=[(1, 'Entrada'), (2, 'Saída')])),
                ('codigo_bb', models.IntegerField()),
                ('tipo_pai', models.ForeignKey(blank=True, limit_choices_to={'tipo_pai': None}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pai', to='caixa.Tipo')),
            ],
        ),
    ]