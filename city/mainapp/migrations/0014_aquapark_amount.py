# Generated by Django 3.2.5 on 2021-08-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_cinema_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='aquapark',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]