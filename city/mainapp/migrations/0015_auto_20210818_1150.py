# Generated by Django 3.2.5 on 2021-08-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_aquapark_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='aquapark',
            name='information',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='visits',
            field=models.CharField(default='', max_length=255, verbose_name='там, где вы были'),
        ),
    ]
