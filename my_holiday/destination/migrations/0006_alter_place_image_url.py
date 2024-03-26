# Generated by Django 4.2.11 on 2024-03-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0005_alter_place_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image_url',
            field=models.URLField(default='https://...', error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, unique=True),
        ),
    ]
