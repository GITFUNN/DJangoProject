# Generated by Django 4.2.4 on 2023-08-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_publication_created_on_alter_comment_publications'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
