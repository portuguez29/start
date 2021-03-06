# Generated by Django 3.0.2 on 2020-02-25 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perm_name', models.CharField(max_length=50, unique=True)),
                ('perm_url', models.SlugField(max_length=100)),
                ('user_create_at', models.DateTimeField(auto_now_add=True)),
                ('user_modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50, unique=True)),
                ('role_description', models.TextField()),
                ('role_create_at', models.DateTimeField(auto_now_add=True)),
                ('role_modified_at', models.DateTimeField(auto_now=True)),
                ('role_permissions', models.ManyToManyField(to='leads.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_user', models.CharField(max_length=50, unique=True)),
                ('user_password', models.CharField(max_length=30)),
                ('user_status', models.IntegerField(choices=[(0, 'Inactivo'), (1, 'Activo'), (2, 'Pausa')], default=1)),
                ('user_create_at', models.DateTimeField(auto_now_add=True)),
                ('user_modified_at', models.DateTimeField(auto_now=True)),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.Role')),
            ],
        ),
        migrations.DeleteModel(
            name='Lead',
        ),
    ]
