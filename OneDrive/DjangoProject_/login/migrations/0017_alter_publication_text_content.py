# Generated by Django 4.2.4 on 2023-08-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_comment_likes_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='text_content',
            field=models.TextField(default=None, max_length=1000),
        ),
    ]