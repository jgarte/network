# Generated by Django 3.0.8 on 2020-08-05 23:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', related_query_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]