# Generated by Django 4.1 on 2023-10-07 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekosApi', '0003_keys_repository_keys_user_keys'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositorycomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
