# Generated by Django 3.0 on 2020-04-03 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criminal_and_victim_details', '0005_auto_20200403_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminaldetail',
            old_name='phone',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='victimdetail',
            old_name='phone',
            new_name='phone_no',
        ),
    ]