# Generated by Django 4.1.4 on 2022-12-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messengers', '0003_message_file_delete_filemessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='del_tag',
            field=models.BooleanField(default=0),
        ),
    ]
