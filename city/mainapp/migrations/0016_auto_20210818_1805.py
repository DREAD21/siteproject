# Generated by Django 3.2.5 on 2021-08-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210818_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aquapark',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
