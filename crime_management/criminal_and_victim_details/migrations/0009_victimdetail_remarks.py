# Generated by Django 3.0 on 2020-04-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminal_and_victim_details', '0008_auto_20200406_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='victimdetail',
            name='remarks',
            field=models.CharField(blank=True, default='unknown', max_length=500, null=True),
        ),
    ]
