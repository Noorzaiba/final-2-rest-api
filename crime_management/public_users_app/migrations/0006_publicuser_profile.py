# Generated by Django 3.0 on 2020-06-04 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_users_app', '0005_auto_20200521_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicuser',
            name='profile',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
