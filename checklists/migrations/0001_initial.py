# Generated by Django 2.0.5 on 2018-05-29 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checklists.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('itens', models.ManyToManyField(through='checklists.ItemTipo', to='checklists.Item')),
            ],
        ),
        migrations.AddField(
            model_name='itemtipo',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checklists.Tipo'),
        ),
        migrations.AlterUniqueTogether(
            name='itemtipo',
            unique_together={('tipo', 'item')},
        ),
    ]
