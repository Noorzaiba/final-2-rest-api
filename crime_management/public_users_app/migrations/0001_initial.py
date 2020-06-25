# Generated by Django 3.0 on 2020-04-17 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=300, unique=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone_no', models.IntegerField()),
                ('gender', models.CharField(max_length=7)),
                ('password', models.CharField(max_length=50)),
                ('adhaar_no', models.PositiveIntegerField(null=True)),
                ('doc', models.DateTimeField(auto_now_add=True)),
                ('dou', models.DateTimeField(auto_now=True)),
                ('email_verification_token', models.CharField(blank=True, default=True, max_length=1000)),
                ('status', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PublicUserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.PositiveIntegerField()),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
                ('resident_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public_users_app.PublicUser')),
            ],
        ),
    ]