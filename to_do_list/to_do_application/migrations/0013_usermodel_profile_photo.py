# Generated by Django 4.1.2 on 2022-11-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_application', '0012_remove_usermodel_tasks_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='profile_photo',
            field=models.ImageField(default='to_do_application/img/profile-icon-9.png', height_field=300, upload_to='static/img', width_field=300),
        ),
    ]
