# Generated by Django 2.2.3 on 2019-07-10 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='phone_number',
        ),
    ]
