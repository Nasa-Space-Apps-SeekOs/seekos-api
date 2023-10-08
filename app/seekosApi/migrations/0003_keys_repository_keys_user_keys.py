# Generated by Django 4.1 on 2023-10-07 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekosApi', '0002_ruserrepositorymember_repository_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'keys',
            },
        ),
        migrations.AddField(
            model_name='repository',
            name='keys',
            field=models.ManyToManyField(related_name='keys_repositories', to='seekosApi.keys'),
        ),
        migrations.AddField(
            model_name='user',
            name='keys',
            field=models.ManyToManyField(related_name='users_keys', to='seekosApi.keys'),
        ),
    ]