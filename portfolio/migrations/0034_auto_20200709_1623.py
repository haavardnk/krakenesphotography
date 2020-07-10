# Generated by Django 3.0.7 on 2020-07-09 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0033_auto_20200709_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontpage',
            name='photo_full',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='photo_full',
        ),
        migrations.AddField(
            model_name='frontpage',
            name='image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Photo'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Photo'),
        ),
    ]
