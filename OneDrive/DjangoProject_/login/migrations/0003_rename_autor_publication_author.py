# Generated by Django 4.2.4 on 2023-08-18 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_publication_autor_publication_text_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='autor',
            new_name='author',
        ),
    ]
