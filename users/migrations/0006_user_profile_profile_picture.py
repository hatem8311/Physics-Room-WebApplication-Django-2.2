# Generated by Django 2.2.3 on 2019-07-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/images/'),
        ),
    ]
