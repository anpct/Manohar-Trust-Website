# Generated by Django 3.0.3 on 2020-03-03 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_gal'),
    ]

    operations = [
        migrations.AddField(
            model_name='gal',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
