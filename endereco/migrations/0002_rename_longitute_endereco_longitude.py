# Generated by Django 4.1 on 2022-08-31 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='longitute',
            new_name='longitude',
        ),
    ]