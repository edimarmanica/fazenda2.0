# Generated by Django 2.0.5 on 2018-05-28 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0004_auto_20180528_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'ordering': ['-dt_nascimento']},
        ),
    ]
