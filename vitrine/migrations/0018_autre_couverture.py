# Generated by Django 4.1.13 on 2024-05-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0017_service_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='autre',
            name='couverture',
            field=models.ImageField(blank=True, null=True, upload_to='Couverture/'),
        ),
    ]
