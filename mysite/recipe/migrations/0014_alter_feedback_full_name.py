# Generated by Django 3.2.6 on 2021-11-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0013_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
