# Generated by Django 3.0.3 on 2020-05-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(),
        ),
    ]