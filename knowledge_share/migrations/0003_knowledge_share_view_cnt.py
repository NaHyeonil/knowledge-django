# Generated by Django 3.2.12 on 2022-03-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_share', '0002_knowledge_share_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge_share',
            name='view_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
