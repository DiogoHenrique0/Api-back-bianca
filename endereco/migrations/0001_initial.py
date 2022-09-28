# Generated by Django 4.1 on 2022-08-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.CharField(max_length=150)),
                ('linha2', models.CharField(blank=True, max_length=150, null=True)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=150)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitute', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
