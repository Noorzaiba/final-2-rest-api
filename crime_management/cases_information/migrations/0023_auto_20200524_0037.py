# Generated by Django 3.0 on 2020-05-24 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases_information', '0022_crimedetail_inves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimedetail',
            name='inves',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
