# Generated by Django 3.0 on 2020-05-24 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases_information', '0020_auto_20200524_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crimedetail',
            name='inves',
        ),
    ]
