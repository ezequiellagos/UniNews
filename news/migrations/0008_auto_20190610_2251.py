# Generated by Django 2.1.3 on 2019-06-11 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20190610_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='numero_region',
            field=models.PositiveIntegerField(unique=True, verbose_name='Número de la región'),
        ),
        migrations.AlterField(
            model_name='universidad',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.Region', to_field='numero_region'),
        ),
    ]
