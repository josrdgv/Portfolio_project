# Generated by Django 4.2.11 on 2024-06-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_login_user_registration_user_profile_cpass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_user',
            name='type',
            field=models.CharField(default=1234, max_length=200),
            preserve_default=False,
        ),
    ]
