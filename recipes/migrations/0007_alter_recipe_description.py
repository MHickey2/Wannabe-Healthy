# Generated by Django 3.2.15 on 2022-10-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='recipe', max_length=200),
        ),
    ]
