# Generated by Django 5.0 on 2023-12-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Socio_app', '0005_post_user_name_alter_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activefriend',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='user_name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='upost',
            old_name='user',
            new_name='username',
        ),
        migrations.AddField(
            model_name='video',
            name='username',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]
