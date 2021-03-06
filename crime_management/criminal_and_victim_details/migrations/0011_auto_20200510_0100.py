# Generated by Django 3.0 on 2020-05-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminal_and_victim_details', '0010_criminaldetail_remarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminaldetailaddress',
            old_name='criminal_id',
            new_name='resident_id',
        ),
        migrations.RenameField(
            model_name='victimdetailaddress',
            old_name='victim_id',
            new_name='resident_id',
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='adhaar_no',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='email',
            field=models.EmailField(blank=True, default='unknown@gmail.com', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='first_name',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='gender',
            field=models.CharField(default='unknown', max_length=8),
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='last_name',
            field=models.CharField(blank=True, default='unknown', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='occupation',
            field=models.CharField(blank=True, default='unknown', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='criminaldetail',
            name='phone_no',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='criminaldetailaddress',
            name='city',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='criminaldetailaddress',
            name='latitude',
            field=models.DecimalField(decimal_places=200, default=0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='criminaldetailaddress',
            name='location',
            field=models.CharField(default='unknown', max_length=300),
        ),
        migrations.AlterField(
            model_name='criminaldetailaddress',
            name='longitude',
            field=models.DecimalField(decimal_places=200, default=0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='criminaldetailaddress',
            name='state',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='criminaldetailaddress',
            name='zip_code',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='adhaar_no',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='email',
            field=models.EmailField(blank=True, default='unknown@gmail.com', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='first_name',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='gender',
            field=models.CharField(default='unknown', max_length=8),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='last_name',
            field=models.CharField(blank=True, default='unknown', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='occupation',
            field=models.CharField(blank=True, default='unknown', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='victimdetail',
            name='phone_no',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='victimdetailaddress',
            name='city',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='victimdetailaddress',
            name='latitude',
            field=models.DecimalField(decimal_places=200, default=0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='victimdetailaddress',
            name='location',
            field=models.CharField(default='unknown', max_length=300),
        ),
        migrations.AlterField(
            model_name='victimdetailaddress',
            name='longitude',
            field=models.DecimalField(decimal_places=200, default=0, max_digits=300),
        ),
        migrations.AlterField(
            model_name='victimdetailaddress',
            name='state',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='victimdetailaddress',
            name='zip_code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
