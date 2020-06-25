# Generated by Django 3.0 on 2020-04-03 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases_information', '0003_auto_20200403_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimedetail',
            name='investigator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]