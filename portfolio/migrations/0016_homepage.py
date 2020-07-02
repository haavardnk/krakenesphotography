# Generated by Django 3.0.3 on 2020-05-09 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_delete_frontpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Photo')),
            ],
        ),
    ]