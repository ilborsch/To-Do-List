# Generated by Django 4.1.2 on 2022-11-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_application', '0020_alter_usermodel_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_photo',
            field=models.ImageField(default='to_do_application/media/user_photos/profile-icon-9.png', max_length=300, upload_to='to_do_application/media/user_photos'),
        ),
    ]
