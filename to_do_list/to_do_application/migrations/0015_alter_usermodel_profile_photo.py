# Generated by Django 4.1.2 on 2022-11-03 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_application', '0014_alter_usermodel_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_photo',
            field=models.ImageField(default='to_do_application/static/to_do_application/img/profile-icon-9.png', max_length=300, upload_to=''),
        ),
    ]
