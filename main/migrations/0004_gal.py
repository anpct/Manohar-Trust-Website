# Generated by Django 3.0.3 on 2020-03-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200303_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery_pics', verbose_name='IMAGES')),
            ],
        ),
    ]
