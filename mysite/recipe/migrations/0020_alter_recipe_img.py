# Generated by Django 3.2.9 on 2021-11-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0019_alter_recipe_recipe_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.ImageField(blank=True, default='recipe_default.jpg', null=True, upload_to='recipe_imgs'),
        ),
    ]
