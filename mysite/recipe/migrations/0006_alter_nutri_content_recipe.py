# Generated by Django 3.2.6 on 2021-11-03 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_alter_recipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutri_content',
            name='Recipe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='recipe.recipe'),
        ),
    ]
