# Generated by Django 4.2.4 on 2023-08-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_alter_profile_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_image',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to='login/media/img_back'),
        ),
    ]