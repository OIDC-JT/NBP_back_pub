# Generated by Django 4.0.1 on 2022-07-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbprun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usenbp',
            name='inputs',
            field=models.JSONField(),
        ),
    ]
