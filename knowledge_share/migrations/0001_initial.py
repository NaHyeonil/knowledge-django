# Generated by Django 3.2.12 on 2022-03-17 05:41

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
            name='Knowledge_Share',
            fields=[
                ('knowledge_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('img1', models.ImageField(blank=True, upload_to='knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S')),
                ('img2', models.ImageField(blank=True, upload_to='knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S')),
                ('img3', models.ImageField(blank=True, upload_to='knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S')),
                ('img4', models.ImageField(blank=True, upload_to='knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S')),
                ('img5', models.ImageField(blank=True, upload_to='knowledge/knowledge_share/%Y/%m/%d/%H/%M/%S')),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-knowledge_no'],
            },
        ),
    ]
