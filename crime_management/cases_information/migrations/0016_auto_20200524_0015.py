# Generated by Django 3.0 on 2020-05-24 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases_information', '0015_auto_20200524_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crimedetail',
            name='investigator_id',
        ),
        migrations.AddField(
            model_name='crimedetail',
            name='investigator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
