# Generated by Django 3.2.6 on 2021-09-13 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_pushkin_card_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article_id',
        ),
    ]
