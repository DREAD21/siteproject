# Generated by Django 3.2.5 on 2021-07-27 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210727_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mane', models.CharField(max_length=255, verbose_name='имя')),
                ('second_name', models.CharField(max_length=255, verbose_name='фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField()),
                ('voted_on', models.DateTimeField(auto_now=True)),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.theater')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
        ),
    ]