# Generated by Django 3.2.5 on 2021-07-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_cinema_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='station',
            field=models.CharField(default='', max_length=255, verbose_name='стацния'),
        ),
    ]