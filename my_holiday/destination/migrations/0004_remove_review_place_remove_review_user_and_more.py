# Generated by Django 4.2.11 on 2024-03-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0003_review_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='place',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='place',
            name='address',
        ),
        migrations.RemoveField(
            model_name='place',
            name='date_visited',
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='place',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], null=True),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]