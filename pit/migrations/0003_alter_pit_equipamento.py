# Generated by Django 4.2.1 on 2023-05-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0002_rename_data_perfu_pit_data_perfuracao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pit',
            name='equipamento',
            field=models.CharField(max_length=254, null=True, verbose_name='equipamento'),
        ),
    ]