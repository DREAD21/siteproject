# Generated by Django 3.2.5 on 2021-07-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210718_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='station',
            field=models.CharField(default='станция', max_length=255),
        ),
    ]
