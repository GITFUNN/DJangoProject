# Generated by Django 4.2.4 on 2023-08-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_alter_profile_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
