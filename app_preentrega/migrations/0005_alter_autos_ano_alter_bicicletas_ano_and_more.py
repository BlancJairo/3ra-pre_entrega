# Generated by Django 4.2.1 on 2023-05-10 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_preentrega', '0004_alter_autos_ano_alter_bicicletas_ano_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos',
            name='ano',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='bicicletas',
            name='ano',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='camiones',
            name='ano',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='camionetas',
            name='ano',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='motos',
            name='ano',
            field=models.CharField(max_length=4),
        ),
    ]