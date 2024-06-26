# Generated by Django 5.0.1 on 2024-04-11 09:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0009_alter_service_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('rue', models.CharField()),
                ('telephone', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Agence/')),
            ],
        ),
        migrations.CreateModel(
            name='Autre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grand_titre', models.CharField(max_length=100)),
                ('petit_titre', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
