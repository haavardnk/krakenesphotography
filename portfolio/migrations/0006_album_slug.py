# Generated by Django 3.0.3 on 2020-04-24 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200424_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default='will-auto-update', unique=True),
        ),
    ]