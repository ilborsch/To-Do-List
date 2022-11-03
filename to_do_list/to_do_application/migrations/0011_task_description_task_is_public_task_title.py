# Generated by Django 4.1.2 on 2022-11-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_application', '0010_usermodel_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='task',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=60),
        ),
    ]
