# Generated by Django 3.0 on 2020-05-10 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases_information', '0010_auto_20200409_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimeliveupdation',
            name='crime_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases_information.CrimeDetail'),
        ),
    ]
