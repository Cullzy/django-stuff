# Generated by Django 3.0.3 on 2020-05-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=168)),
                ('the_type', models.CharField(max_length=168)),
                ('hp', models.IntegerField(max_length=168)),
            ],
        ),
    ]