# Generated by Django 3.2.6 on 2021-09-14 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0023_auto_20210913_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(default='', max_length=255)),
                ('meal_del', models.CharField(blank=True, max_length=30)),
                ('site_del', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('vk_link', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='comment',
            name='article_id',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
