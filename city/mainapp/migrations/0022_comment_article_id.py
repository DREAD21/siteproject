# Generated by Django 3.2.6 on 2021-09-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_remove_comment_article_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
