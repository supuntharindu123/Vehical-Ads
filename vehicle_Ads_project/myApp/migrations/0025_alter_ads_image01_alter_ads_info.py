# Generated by Django 5.1.3 on 2025-01-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0024_alter_ads_image01'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image01',
            field=models.ImageField(upload_to='vehicles'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='info',
            field=models.CharField(max_length=5000),
        ),
    ]
