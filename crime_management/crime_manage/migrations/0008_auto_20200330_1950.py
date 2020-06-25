# Generated by Django 3.0 on 2020-03-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_manage', '0007_auto_20200321_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigatorprofile',
            name='email_verification_token',
            field=models.CharField(blank=True, default=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='investigatorprofile',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]