# Generated by Django 3.0 on 2020-05-21 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_users_app', '0004_auto_20200510_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicuseraddress',
            name='latitude',
            field=models.DecimalField(decimal_places=15, default=0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='publicuseraddress',
            name='longitude',
            field=models.DecimalField(decimal_places=15, default=0, max_digits=300),
        ),
    ]
