# Generated by Django 4.1.2 on 2022-10-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
