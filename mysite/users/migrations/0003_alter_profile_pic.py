# Generated by Django 3.2.6 on 2021-11-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics'),
        ),
    ]
