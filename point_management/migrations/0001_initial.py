# Generated by Django 3.2.12 on 2022-04-06 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PointManagement',
            fields=[
                ('point_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('approval', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-point_no'],
            },
        ),
    ]
