# Generated by Django 4.0.6 on 2022-11-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(upload_to='pacientes', verbose_name='foto'),
        ),
    ]