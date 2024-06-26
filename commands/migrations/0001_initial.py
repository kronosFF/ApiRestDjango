# Generated by Django 5.0.3 on 2024-03-29 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre Comando')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('parameters', models.TextField(verbose_name='Parámetros')),
            ],
            options={
                'verbose_name': 'Comando',
                'verbose_name_plural': 'Productos',
                'ordering': ['name'],
            },
        ),
    ]
