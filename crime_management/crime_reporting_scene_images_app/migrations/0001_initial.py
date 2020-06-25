# Generated by Django 3.0 on 2020-06-23 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crime_reporting_app', '0008_auto_20200520_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeReportingSceneImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=300)),
                ('crime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_reporting_app.CrimeReported')),
            ],
        ),
    ]
