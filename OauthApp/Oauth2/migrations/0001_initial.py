# Generated by Django 3.1.1 on 2020-12-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('access_token', models.CharField(default='', max_length=360)),
                ('refresh_token', models.CharField(default='', max_length=360)),
            ],
        ),
    ]
