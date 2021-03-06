# Generated by Django 2.1.3 on 2019-06-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190610_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='letra_region',
            field=models.CharField(default=None, max_length=5, verbose_name='Numeros romanos de región'),
        ),
        migrations.AlterField(
            model_name='region',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre de la región'),
        ),
        migrations.AlterField(
            model_name='region',
            name='numero_region',
            field=models.PositiveIntegerField(verbose_name='Número de la región'),
        ),
    ]
