# Generated by Django 3.0 on 2020-05-10 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeReported',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_crime', models.CharField(blank=True, choices=[('Robbery', 'Robbery'), ('Murder', 'Murder'), ('Acid Throwing', 'Acid Throwing'), ('Ragging', 'Ragging'), ('Property', 'Property '), ('Others', 'Others'), ('Smuggling', 'Smuggling'), ('Vandalism', 'Vandalism'), ('Torture', 'Torture')], max_length=300, null=True)),
                ('description', models.CharField(max_length=400)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('doc', models.DateTimeField(auto_now_add=True)),
                ('dou', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='null', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeReportedLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.PositiveIntegerField()),
                ('longitude', models.DecimalField(decimal_places=200, max_digits='300')),
                ('latitude', models.DecimalField(decimal_places=200, max_digits='300')),
                ('crime_reported', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crime_reporting_app.CrimeReported')),
            ],
        ),
    ]
