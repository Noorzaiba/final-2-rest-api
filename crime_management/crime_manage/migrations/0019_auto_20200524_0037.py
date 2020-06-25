# Generated by Django 3.0 on 2020-05-24 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crime_manage', '0018_auto_20200414_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigatoraddress',
            name='latitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='investigatoraddress',
            name='longitude',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='investigatoraddress',
            name='resident_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='investigatorsadministrativedetail',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='investigatorsadministrativedetail',
            name='salary',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=300),
        ),
    ]