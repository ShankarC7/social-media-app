# Generated by Django 5.0 on 2023-12-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Socio_app', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(upload_to='profile_pics/')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
