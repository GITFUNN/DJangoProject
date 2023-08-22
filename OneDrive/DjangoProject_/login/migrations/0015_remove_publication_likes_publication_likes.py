# Generated by Django 4.2.4 on 2023-08-22 18:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0014_publication_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='likes',
        ),
        migrations.AddField(
            model_name='publication',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]