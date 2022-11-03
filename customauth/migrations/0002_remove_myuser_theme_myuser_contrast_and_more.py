# Generated by Django 4.1.2 on 2022-11-03 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='theme',
        ),
        migrations.AddField(
            model_name='myuser',
            name='contrast',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='font_size',
            field=models.FloatField(default=13, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]