# Generated by Django 3.1.1 on 2020-09-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='figures',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]