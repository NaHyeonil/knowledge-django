# Generated by Django 3.2.12 on 2022-04-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220318_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='credit',
        ),
        migrations.AddField(
            model_name='user',
            name='accumulated_point',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='available_point',
            field=models.IntegerField(default=0),
        ),
    ]
