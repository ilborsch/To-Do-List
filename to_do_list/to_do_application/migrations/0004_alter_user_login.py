# Generated by Django 4.1.2 on 2022-10-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_application', '0003_alter_user_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
