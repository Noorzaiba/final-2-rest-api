# Generated by Django 3.0 on 2020-03-28 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('occurance_time', models.DateTimeField(null=True)),
                ('doc', models.DateTimeField(auto_now_add=True)),
                ('dou', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='null', max_length=200)),
                ('investigator_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeLocationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('crime_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cases_information.CrimeDetail')),
            ],
        ),
    ]
