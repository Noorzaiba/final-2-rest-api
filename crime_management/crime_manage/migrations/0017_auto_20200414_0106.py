# Generated by Django 3.0 on 2020-04-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_manage', '0016_auto_20200413_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigatorsadministrativedetail',
            name='achivements',
            field=models.CharField(default='unknown', max_length=300),
        ),
        migrations.AlterField(
            model_name='investigatorsadministrativedetail',
            name='position',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='investigatorsadministrativedetail',
            name='salary',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=300),
        ),
    ]