# Generated by Django 4.2.4 on 2023-08-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_alter_publication_text_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
