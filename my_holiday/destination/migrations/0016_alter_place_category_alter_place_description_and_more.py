# Generated by Django 4.2.11 on 2024-04-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0015_remove_place_image_url_place_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(blank=True, choices=[('Mountain', 'Mountain'), ('Sea', 'Sea'), ('Historical Site', 'Historical Site'), ('City', 'City'), ('Spa', 'Spa'), ('Wine Tourism', 'Wine Tourism')], max_length=100, null=True, verbose_name='Hotel category'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(verbose_name='Hotel description'),
        ),
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.CharField(max_length=200, verbose_name='Hotel location'),
        ),
        migrations.AlterField(
            model_name='place',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], null=True, verbose_name='Hotel rating'),
        ),
    ]
