# Generated by Django 4.2.1 on 2023-05-24 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pit',
            old_name='data_perfu',
            new_name='data_perfuracao',
        ),
        migrations.RenameField(
            model_name='pit',
            old_name='equipament',
            new_name='equipamento',
        ),
        migrations.RenameField(
            model_name='pit',
            old_name='profundida',
            new_name='profundidade',
        ),
        migrations.RenameField(
            model_name='pit',
            old_name='proprietar',
            new_name='proprietario',
        ),
    ]