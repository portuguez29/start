# Generated by Django 3.0.2 on 2020-02-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20200226_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_file',
            field=models.ImageField(blank=True, upload_to='images/%Y/%D/'),
        ),
    ]
