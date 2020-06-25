# Generated by Django 3.0 on 2020-04-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminal_and_victim_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminalvictimaddress',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='criminalvictimaddress',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='criminalvictimaddress',
            name='location',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='criminalvictimaddress',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='criminalvictimaddress',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='criminalvictimaddress',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
