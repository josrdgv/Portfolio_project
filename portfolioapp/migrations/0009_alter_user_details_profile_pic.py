# Generated by Django 4.2.11 on 2024-06-11 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0008_alter_user_details_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='profile_pic',
            field=models.ImageField(default=1234, upload_to='profile_pic/'),
            preserve_default=False,
        ),
    ]
