# Generated by Django 3.0.2 on 2020-02-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_auto_20200226_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistant',
            name='assi_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assistant',
            name='assi_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assistant',
            name='assi_email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='assistant',
            name='assi_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_cost',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_final_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='clie_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='clie_email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='clie_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='lawy_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='lawy_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='lawy_email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='lawy_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='reco_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sche_color',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sche_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sche_duration',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='type_case',
            name='type_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.IntegerField(choices=[(0, 'Inactivos'), (1, 'Activos'), (2, 'Vacaciones')], default=1),
        ),
    ]
